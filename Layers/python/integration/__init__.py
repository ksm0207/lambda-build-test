from .lambda_app import LambdaApp
import os

try:
    from secretManager import get_secret
except ImportError:
    from Layers.python.secretManager import get_secret

__all__ = ["app"]


app = LambdaApp(secret_data=get_secret(os.environ.get("ENV")))
