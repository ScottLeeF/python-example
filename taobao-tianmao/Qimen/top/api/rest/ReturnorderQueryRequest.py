'''
Created by auto_sdk on 2016.08.24
'''
from top.api.base import RestApi


class ReturnorderQueryRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.extendProps = None
        self.ownerCode = None
        self.page = None
        self.pageSize = None
        self.returnOrderCode = None
        self.returnOrderId = None
        self.warehouseCode = None

    def getapiname(self):
        return 'taobao.qimen.returnorder.query'
