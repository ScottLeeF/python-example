'''
Created by auto_sdk on 2018.05.18
'''
from top.api.base import RestApi


class ShopSynchronizeRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.actionType = None
        self.shop = None

    def getapiname(self):
        return 'taobao.qimen.shop.synchronize'
