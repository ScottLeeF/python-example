'''
Created by auto_sdk on 2016.08.24
'''
from top.api.base import RestApi


class OrderstatusBatchqueryRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.currentPage = None
        self.endTime = None
        self.extendProps = None
        self.orderType = None
        self.ownerCode = None
        self.pageSize = None
        self.startTime = None
        self.warehouseCode = None

    def getapiname(self):
        return 'taobao.qimen.orderstatus.batchquery'
