'''
Created by auto_sdk on 2018.09.12
'''
from top.api.base import RestApi


class CainiaoEndpointLockerTopOrderNoticesendQueryRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.getter_phone = None
        self.mail_no = None
        self.station_id = None

    def getapiname(self):
        return 'cainiao.endpoint.locker.top.order.noticesend.query'
