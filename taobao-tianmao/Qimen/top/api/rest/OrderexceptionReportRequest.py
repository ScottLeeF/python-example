'''
Created by auto_sdk on 2018.08.16
'''
from top.api.base import RestApi


class OrderexceptionReportRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.createTime = None
        self.deliveryOrderCode = None
        self.deliveryOrderId = None
        self.expressCode = None
        self.extendProps = None
        self.logisticsCode = None
        self.messageDesc = None
        self.messageId = None
        self.messageType = None
        self.orderLines = None
        self.orderType = None
        self.remark = None
        self.warehouseCode = None

    def getapiname(self):
        return 'taobao.qimen.orderexception.report'
