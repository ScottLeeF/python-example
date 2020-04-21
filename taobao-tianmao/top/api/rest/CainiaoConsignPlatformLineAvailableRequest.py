'''
Created by auto_sdk on 2020.02.21
'''
from top.api.base import RestApi


class CainiaoConsignPlatformLineAvailableRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.line_available_d_t_o = None

    def getapiname(self):
        return 'cainiao.consign.platform.line.available'
