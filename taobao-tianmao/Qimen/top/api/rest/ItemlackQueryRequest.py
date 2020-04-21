'''
Created by auto_sdk on 2016.07.21
'''
from top.api.base import RestApi


class ItemlackQueryRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.deliveryOrderCode = None
        self.deliveryOrderId = None
        self.extendProps = None
        self.ownerCode = None
        self.page = None
        self.pageSize = None
        self.warehouseCode = None

    def getapiname(self):
        return 'taobao.qimen.itemlack.query'
