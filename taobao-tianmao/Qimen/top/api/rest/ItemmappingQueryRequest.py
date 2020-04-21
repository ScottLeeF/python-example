'''
Created by auto_sdk on 2019.11.20
'''
from top.api.base import RestApi


class ItemmappingQueryRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.itemId = None
        self.ownerCode = None
        self.queryType = None
        self.shopItemId = None
        self.skuId = None

    def getapiname(self):
        return 'taobao.qimen.itemmapping.query'
