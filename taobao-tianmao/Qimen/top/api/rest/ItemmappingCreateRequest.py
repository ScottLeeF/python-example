'''
Created by auto_sdk on 2018.07.25
'''
from top.api.base import RestApi


class ItemmappingCreateRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.actionType = None
        self.itemId = None
        self.itemSource = None
        self.ownerCode = None
        self.shopItemId = None
        self.shopNick = None
        self.skuId = None

    def getapiname(self):
        return 'taobao.qimen.itemmapping.create'
