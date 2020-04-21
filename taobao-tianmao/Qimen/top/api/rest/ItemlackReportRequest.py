'''
Created by auto_sdk on 2018.07.25
'''
from top.api.base import RestApi


class ItemlackReportRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.createTime = None
        self.deliveryOrderCode = None
        self.deliveryOrderId = None
        self.extendProps = None
        self.items = None
        self.outBizCode = None
        self.remark = None
        self.warehouseCode = None

    def getapiname(self):
        return 'taobao.qimen.itemlack.report'
