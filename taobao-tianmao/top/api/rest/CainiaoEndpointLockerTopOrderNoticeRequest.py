'''
Created by auto_sdk on 2018.07.25
'''
from top.api.base import RestApi


class CainiaoEndpointLockerTopOrderNoticeRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.mail_no = None
        self.order_code = None
        self.scene_code = None
        self.station_id = None

    def getapiname(self):
        return 'cainiao.endpoint.locker.top.order.notice'
