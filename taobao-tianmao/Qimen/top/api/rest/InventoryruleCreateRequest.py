'''
Created by auto_sdk on 2018.07.25
'''
from top.api.base import RestApi


class InventoryruleCreateRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.inventoryRules = None
        self.ownerCode = None

    def getapiname(self):
        return 'taobao.qimen.inventoryrule.create'
