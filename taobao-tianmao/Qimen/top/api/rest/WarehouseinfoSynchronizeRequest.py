'''
Created by auto_sdk on 2019.10.23
'''
from top.api.base import RestApi


class WarehouseinfoSynchronizeRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.ownerCode = None
        self.ownerName = None
        self.warehouseInfos = None

    def getapiname(self):
        return 'taobao.qimen.warehouseinfo.synchronize'
