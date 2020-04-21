'''
Created by auto_sdk on 2019.03.12
'''
from top.api.base import RestApi


class ReturnpackageReportRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.order = None
        self.packages = None

    def getapiname(self):
        return 'taobao.qimen.returnpackage.report'
