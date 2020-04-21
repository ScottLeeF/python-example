'''
Created by auto_sdk on 2019.11.20
'''
from top.api.base import RestApi


class ReturnapplyReportRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.createDate = None
        self.createEmp = None
        self.expressCode = None
        self.items = None
        self.logisticsCode = None
        self.logisticsName = None
        self.orderCode = None
        self.orderId = None
        self.receiverInfo = None
        self.remark = None
        self.shopCode = None
        self.warehouseCode = None

    def getapiname(self):
        return 'taobao.qimen.returnapply.report'
