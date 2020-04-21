'''
Created by auto_sdk on 2018.08.01
'''
from top.api.base import RestApi


class InventoryReportRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.adjustType = None
        self.checkOrderCode = None
        self.checkOrderId = None
        self.checkTime = None
        self.currentPage = None
        self.extendProps = None
        self.items = None
        self.orderType = None
        self.outBizCode = None
        self.ownerCode = None
        self.pageSize = None
        self.remark = None
        self.totalPage = None
        self.warehouseCode = None

    def getapiname(self):
        return 'taobao.qimen.inventory.report'
