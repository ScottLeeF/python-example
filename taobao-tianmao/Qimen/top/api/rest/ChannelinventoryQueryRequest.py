'''
Created by auto_sdk on 2018.07.25
'''
from top.api.base import RestApi


class ChannelinventoryQueryRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.channelCodes = None
        self.itemCodes = None
        self.ownerCode = None
        self.warehouseCodes = None

    def getapiname(self):
        return 'taobao.qimen.channelinventory.query'
