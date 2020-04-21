'''
Created by auto_sdk on 2019.02.13
'''
from top.api.base import RestApi


class StockQueryRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.batchCode = None
        self.expireDate = None
        self.extendProps = None
        self.inventoryType = None
        self.itemCode = None
        self.itemId = None
        self.ownerCode = None
        self.page = None
        self.pageSize = None
        self.productDate = None
        self.remark = None
        self.warehouseCode = None

    def getapiname(self):
        return 'taobao.qimen.stock.query'
