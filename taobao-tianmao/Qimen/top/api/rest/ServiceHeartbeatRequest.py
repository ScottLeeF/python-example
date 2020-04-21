'''
Created by auto_sdk on 2019.10.29
'''
from top.api.base import RestApi


class ServiceHeartbeatRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.serialNumber = None

    def getapiname(self):
        return 'taobao.qimen.service.heartbeat'
