'''
Created by auto_sdk on 2018.01.18
'''
from top.api.base import RestApi


class InventorycheckQueryRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.checkOrderCode = None
        self.checkOrderId = None
        self.extendProps = None
        self.ownerCode = None
        self.page = None
        self.pageSize = None
        self.warehouseCode = None

    def getapiname(self):
        return 'taobao.qimen.inventorycheck.query'
