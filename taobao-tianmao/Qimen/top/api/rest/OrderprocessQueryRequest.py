'''
Created by auto_sdk on 2018.07.25
'''
from top.api.base import RestApi


class OrderprocessQueryRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.extendProps = None
        self.orderCode = None
        self.orderId = None
        self.orderSourceCode = None
        self.orderType = None
        self.ownerCode = None
        self.remark = None
        self.warehouseCode = None

    def getapiname(self):
        return 'taobao.qimen.orderprocess.query'
