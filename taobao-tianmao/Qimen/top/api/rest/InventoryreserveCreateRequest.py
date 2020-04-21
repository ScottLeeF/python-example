'''
Created by auto_sdk on 2016.08.04
'''
from top.api.base import RestApi


class InventoryreserveCreateRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.extendProps = None
        self.itemInventories = None
        self.maxWarehouseNum = None
        self.orderCode = None
        self.orderSource = None
        self.ownerCode = None
        self.receiverInfo = None
        self.warehouseCode = None

    def getapiname(self):
        return 'taobao.qimen.inventoryreserve.create'
