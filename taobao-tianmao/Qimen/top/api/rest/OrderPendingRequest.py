'''
Created by auto_sdk on 2018.07.25
'''
from top.api.base import RestApi


class OrderPendingRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.actionType = None
        self.extendProps = None
        self.orderCode = None
        self.orderId = None
        self.orderType = None
        self.ownerCode = None
        self.reason = None
        self.warehouseCode = None

    def getapiname(self):
        return 'taobao.qimen.order.pending'
