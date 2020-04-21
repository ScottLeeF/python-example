'''
Created by auto_sdk on 2018.07.25
'''
from top.api.base import RestApi


class CombineitemSynchronizeRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.extendProps = None
        self.itemCode = None
        self.itemId = None
        self.items = None
        self.ownerCode = None
        self.warehouseCode = None

    def getapiname(self):
        return 'taobao.qimen.combineitem.synchronize'
