'''
Created by auto_sdk on 2019.08.19
'''
from top.api.base import RestApi


class ReturnorderCreateRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.extendProps = None
        self.itemList = None
        self.orderLines = None
        self.returnOrder = None

    def getapiname(self):
        return 'taobao.qimen.returnorder.create'
