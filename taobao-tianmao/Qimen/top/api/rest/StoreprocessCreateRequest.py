'''
Created by auto_sdk on 2018.07.25
'''
from top.api.base import RestApi


class StoreprocessCreateRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.extendProps = None
        self.materialitems = None
        self.orderCreateTime = None
        self.orderType = None
        self.planQty = None
        self.planTime = None
        self.processOrderCode = None
        self.productitems = None
        self.remark = None
        self.serviceType = None
        self.warehouseCode = None

    def getapiname(self):
        return 'taobao.qimen.storeprocess.create'
