'''
Created by auto_sdk on 2019.07.05
'''
from top.api.base import RestApi


class ItemsSynchronizeRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.actionType = None
        self.extendProps = None
        self.items = None
        self.ownerCode = None
        self.warehouseCode = None

    def getapiname(self):
        return 'taobao.qimen.items.synchronize'
