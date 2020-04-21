'''
Created by auto_sdk on 2018.07.26
'''
from top.api.base import RestApi


class EntryorderQueryRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.entryOrderCode = None
        self.entryOrderId = None
        self.extOrderCode = None
        self.extendProps = None
        self.orderType = None
        self.ownerCode = None
        self.page = None
        self.pageSize = None
        self.remark = None
        self.warehouseCode = None

    def getapiname(self):
        return 'taobao.qimen.entryorder.query'
