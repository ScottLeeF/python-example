'''
Created by auto_sdk on 2019.10.25
'''
from top.api.base import RestApi


class TransferorderCreateRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.attributes = None
        self.erpOrderCode = None
        self.expectStartTime = None
        self.fromStoreCode = None
        self.ownerCode = None
        self.toStoreCode = None
        self.transferItems = None

    def getapiname(self):
        return 'taobao.qimen.transferorder.create'
