'''
Created by auto_sdk on 2019.07.31
'''
from top.api.base import RestApi


class CainiaoEndpointLockerTopOrderTrackingNewRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.track_info = None

    def getapiname(self):
        return 'cainiao.endpoint.locker.top.order.tracking.new'
