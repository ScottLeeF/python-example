'''
Created by auto_sdk on 2019.12.23
'''
from top.api.base import RestApi


class EntryorderCreateRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.entryOrder = None
        self.extendProps = None
        self.items = None
        self.orderLines = None

    def getapiname(self):
        return 'taobao.qimen.entryorder.create'
