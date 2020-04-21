'''
Created by auto_sdk on 2018.07.25
'''
from top.api.base import RestApi


class StoreprocessConfirmRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.actualQty = None
        self.extendProps = None
        self.materialitems = None
        self.orderCompleteTime = None
        self.orderType = None
        self.outBizCode = None
        self.ownerCode = None
        self.processOrderCode = None
        self.processOrderId = None
        self.productitems = None
        self.remark = None

    def getapiname(self):
        return 'taobao.qimen.storeprocess.confirm'
