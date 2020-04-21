'''
Created by auto_sdk on 2018.08.08
'''
from top.api.base import RestApi


class TmallExchangeGetRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.dispute_id = None
        self.fields = None

    def getapiname(self):
        return 'tmall.exchange.get'
