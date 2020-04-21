'''
Created by auto_sdk on 2018.07.26
'''
from top.api.base import RestApi


class DeliveryorderQueryRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.deliveryOrderCode = None
        self.deliveryOrderId = None
        self.extendProps = None
        self.orderCode = None
        self.orderId = None
        self.orderSourceCode = None
        self.ownerCode = None
        self.page = None
        self.pageSize = None
        self.remark = None
        self.status = None
        self.warehouseCode = None

    def getapiname(self):
        return 'taobao.qimen.deliveryorder.query'
