'''
Created by auto_sdk on 2019.07.05
'''
from top.api.base import RestApi


class SingleitemQueryRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.itemCode = None
        self.itemId = None
        self.ownerCode = None

    def getapiname(self):
        return 'taobao.qimen.singleitem.query'
