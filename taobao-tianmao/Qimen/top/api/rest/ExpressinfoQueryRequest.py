'''
Created by auto_sdk on 2018.07.25
'''
from top.api.base import RestApi


class ExpressinfoQueryRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.expressCode = None
        self.extendProps = None
        self.ownerCode = None

    def getapiname(self):
        return 'taobao.qimen.expressinfo.query'
