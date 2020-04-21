'''
Created by auto_sdk on 2018.07.26
'''
from top.api.base import RestApi


class SnReportRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.currentPage = None
        self.deliveryOrder = None
        self.extendProps = None
        self.items = None
        self.pageSize = None
        self.totalPage = None

    def getapiname(self):
        return 'taobao.qimen.sn.report'
