'''
Created by auto_sdk on 2018.07.25
'''
from top.api.base import RestApi


class OrderSnReportRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.currentPage = None
        self.extendProps = None
        self.items = None
        self.order = None
        self.pageSize = None
        self.totalPage = None

    def getapiname(self):
        return 'taobao.qimen.order.sn.report'
