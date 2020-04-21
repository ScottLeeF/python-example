'''
Created by auto_sdk on 2018.08.09
'''
from top.api.base import RestApi


class TmallExchangeMessagesGetRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.dispute_id = None
        self.fields = None
        self.operator_roles = None
        self.page_no = None
        self.page_size = None

    def getapiname(self):
        return 'tmall.exchange.messages.get'
