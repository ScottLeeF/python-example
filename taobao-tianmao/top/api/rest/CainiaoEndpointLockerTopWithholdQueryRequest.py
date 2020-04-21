'''
Created by auto_sdk on 2018.07.25
'''
from top.api.base import RestApi


class CainiaoEndpointLockerTopWithholdQueryRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.company_code = None
        self.open_user_id = None
        self.order_type = None

    def getapiname(self):
        return 'cainiao.endpoint.locker.top.withhold.query'
