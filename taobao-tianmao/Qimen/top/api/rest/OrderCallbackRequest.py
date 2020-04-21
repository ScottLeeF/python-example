'''
Created by auto_sdk on 2018.07.25
'''
from top.api.base import RestApi


class OrderCallbackRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.deliveryOrderCode = None
        self.expressCode = None
        self.orderId = None
        self.ownerCode = None
        self.warehouseCode = None

    def getapiname(self):
        return 'taobao.qimen.order.callback'
