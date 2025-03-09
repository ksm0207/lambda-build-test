from typing import Callable, Any, Dict
import logging

try:
    import pymysql
    from pymysql.connections import Connection
    from pymysql.cursors import DictCursor
    from humps import decamelize, camelize
except ImportError:
    import Layers.python.pymysql as pymysql
    from Layers.python.pymysql.connections import Connection
    from Layers.python.pymysql.cursors import DictCursor
    from Layers.python.humps import decamelize, camelize

logger = logging.getLogger("LambdaApp")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

__all__ = ["LambdaApp"]

SecretData = Dict[str, str]


def _replace_query(query: Dict[str, str]) -> Dict[str, Any]:
    result = dict()
    for k, v in query.items():
        logger.info(f"Key => {k}")
        logger.info(f"Value => {v}, {type(v)}")
        result.setdefault(k.replace("-", "_"), int(v) if v.isdigit() else v)

    logger.info(f"{result}")
    return result


class LambdaApp:
    """
    AWS Gateway with Lambda app.
    Need Python >= 3.10
    """

    def __init__(self, secret_data: SecretData):
        self.db_info: Dict = {
            "host": secret_data.get("rds_host"),
            "port": 3306,
            "user": secret_data.get("name"),
            "database": secret_data.get("db_name"),
            "password": secret_data.get("password"),
            "charset": "UTF8MB4"
        }

        self.connection: Connection | None = None
        self.cursor: DictCursor | None = None

        self.secret_data = secret_data

    def build(self) -> Callable[[Callable[..., Dict[str, Any]]], Callable[..., Dict[str, Any]]]:
        """
        lambda_handler 함수 전용 데코레이터입니다.
        사용하기 위해서는 AWS Gateway에서 통합요청 -> aws gateway passthrough 설정이 필요합니다.
        """

        def decorator(function: Callable[..., Dict[str, Any]]) -> Callable[..., Dict[str, Any]]:
            def wrapper(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
                self.connection = pymysql.connect(**self.db_info)
                self.cursor = self.connection.cursor(cursor=DictCursor)
                event.setdefault("connection", self.connection)
                event.setdefault("cursor", self.cursor)
                body: Dict = event.get("body-json")
                params: Dict = event.get("params")
                event.setdefault("body", decamelize(body))
                event.setdefault("headers", params.get("header"))
                event.setdefault("path", params.get("path"))
                event.setdefault("query", _replace_query(params.get("querystring")))
                event.setdefault("secret", self.secret_data)

                del event["body-json"]

                logger.info(f"Lambda Event => {event}")
                logger.info(f"Body => {body}")
                logger.info(f"Params => {params}")

                try:
                    result = camelize(function(event, context))
                    logger.info(f"Result => {result}")
                    return result
                except Exception as e:
                    logger.error(e.args)
                    raise e
                finally:
                    self.cursor.close()
                    self.connection.close()

            return wrapper

        return decorator
