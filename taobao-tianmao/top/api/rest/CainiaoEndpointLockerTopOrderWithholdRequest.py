'''
Created by auto_sdk on 2018.07.25
'''
from top.api.base import RestApi


class CainiaoEndpointLockerTopOrderWithholdRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.company_code = None
        self.extra = None
        self.gui_id = None
        self.mail_no = None
        self.open_user_id = None
        self.order_code = None
        self.order_type = None
        self.total_fee = None

    def getapiname(self):
        return 'cainiao.endpoint.locker.top.order.withhold'
