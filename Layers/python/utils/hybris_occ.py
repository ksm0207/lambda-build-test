import json
from urllib import request

class HybrisOcc:
    def __init__(self, SECRET_KEY):
        self.domain = SECRET_KEY['HYBRIS_DOMAIN']
        self.client_id = SECRET_KEY['HYBRIS_CLIENT_ID']
        self.client_secret = SECRET_KEY['HYBRIS_CLIENT_SECRET']
        self.set_token()
        self.headers = {'Accept ': 'application/json', 'Content-Type ': 'application/json', 'Authorization': 'bearer '+self.token}

    def set_token(self):  # 토큰발급
        try:
            url = self.domain+'/authorizationserver/oauth/token?grant_type=client_credentials&client_id=' + \
                self.client_id+'&client_secret='+self.client_secret
            headers = {'Accept ': 'application/json'}
            req = request.Request(url, headers=headers, method='POST')
            res = request.urlopen(req)
            rescode = res.status

            if(rescode == 200):
                result = res.read()
                self.token = json.loads(result)['access_token']
            else:
                result = rescode

        except Exception as ex:
            print("error: "+ex.__str__())
            err = {
                "type": "token",
                "message": ex.__str__()
            }
            raise Exception(err)

        return json.loads(result)

    # Method Name : trade_in_account_info
    # Desc        : 회원 정보 조회
    # Param       : uid ==> 회원 uid
    
    #               amwayBusinessNature ==> AmwayBusinessNature_1,2,4,7
    def trade_in_account_info(self, param):  # 회원 정보 조회
        try:
            url = self.domain+'/api/v2/amwaykorea/mylab/customers/Uid/' + param['uid']
            req = request.Request(url, headers=self.headers, method="GET")
            res = request.urlopen(req)
            rescode = res.status

            if(rescode == 200):
                result = res.read()
            else:
                result = rescode

        except Exception as ex:
            print("error: "+ex.__str__())
            err = {
                "type": "trade_in_account_info",
                "message": ex.__str__()
            }
            raise Exception(err)

        return json.loads(result)


    def trade_in_coupon_reg(self, param):  # 쿠폰 발급
        try:
            url = self.domain+'/api/v2/amwaykorea/users/' + param['abo_no'] + '/coupon/assign?couponIdList=' + param['coupon_id_list']
            req = request.Request(url, headers=self.headers, method="GET")
            res = request.urlopen(req)
            rescode = res.status

            if(rescode == 200):
                result = res.read()
            else:
                result = rescode

        except Exception as ex:
            print("error: "+ex.__str__())
            err = {
                "type": "trade_in_coupon_reg",
                "message": ex.__str__()
            }
            raise Exception(err)

        return json.loads(result)

    def trade_in_coupon_cancel(self, param):  # 쿠폰 발급 취소
        try:
            url = self.domain+'/api/v2/amwaykorea/users/' + param['abo_no'] + '/coupon/undo?couponIdList=' + param['coupon_id_list']
            req = request.Request(url, headers=self.headers, method="GET")
            res = request.urlopen(req)
            rescode = res.status

            if(rescode == 200):
                result = res.read()
            else:
                result = rescode

        except Exception as ex:
            print("error: "+ex.__str__())
            err = {
                "type": "trade_in_coupon_cancel",
                "message": ex.__str__()
            }
            raise Exception(err)

        return json.loads(result)
