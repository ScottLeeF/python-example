'''
Created by auto_sdk on 2018.07.25
'''
from top.api.base import RestApi


class CombineitemQueryRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.extendProps = None
        self.itemId = None
        self.ownerCode = None

    def getapiname(self):
        return 'taobao.qimen.combineitem.query'
