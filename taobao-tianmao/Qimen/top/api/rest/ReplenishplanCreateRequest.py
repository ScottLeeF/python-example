'''
Created by auto_sdk on 2016.08.17
'''
from top.api.base import RestApi


class ReplenishplanCreateRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.extendProps = None
        self.gmtDeadTime = None
        self.items = None
        self.orderCode = None
        self.userId = None
        self.warehouseCode = None

    def getapiname(self):
        return 'taobao.qimen.replenishplan.create'
