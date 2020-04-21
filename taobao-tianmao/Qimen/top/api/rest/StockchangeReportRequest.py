'''
Created by auto_sdk on 2018.07.26
'''
from top.api.base import RestApi


class StockchangeReportRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.currentPage = None
        self.extendProps = None
        self.items = None
        self.orderCode = None
        self.orderType = None
        self.ownerCode = None
        self.pageSize = None
        self.remark = None
        self.totalPage = None
        self.warehouseCode = None

    def getapiname(self):
        return 'taobao.qimen.stockchange.report'
