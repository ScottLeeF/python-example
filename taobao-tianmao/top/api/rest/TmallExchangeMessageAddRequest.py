'''
Created by auto_sdk on 2018.08.09
'''
from top.api.base import RestApi


class TmallExchangeMessageAddRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.content = None
        self.dispute_id = None
        self.fields = None
        self.message_pics = None

    def getapiname(self):
        return 'tmall.exchange.message.add'

    def getMultipartParas(self):
        return ['message_pics']
