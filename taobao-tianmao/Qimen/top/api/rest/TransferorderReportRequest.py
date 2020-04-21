'''
Created by auto_sdk on 2018.07.25
'''
from top.api.base import RestApi


class TransferorderReportRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.confirmInTime = None
        self.confirmOutTime = None
        self.createTime = None
        self.erpOrderCode = None
        self.fromWarehouseCode = None
        self.items = None
        self.orderStatus = None
        self.ownerCode = None
        self.toWarehouseCode = None
        self.transferInOrderCode = None
        self.transferOrderCode = None
        self.transferOutOrderCode = None

    def getapiname(self):
        return 'taobao.qimen.transferorder.report'
