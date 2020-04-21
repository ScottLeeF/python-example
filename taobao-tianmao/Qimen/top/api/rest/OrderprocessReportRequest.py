'''
Created by auto_sdk on 2018.07.26
'''
from top.api.base import RestApi


class OrderprocessReportRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.extendProps = None
        self.order = None
        self.process = None
        self.remark = None

    def getapiname(self):
        return 'taobao.qimen.orderprocess.report'
