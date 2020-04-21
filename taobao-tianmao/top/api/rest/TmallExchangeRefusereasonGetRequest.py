'''
Created by auto_sdk on 2018.08.09
'''
from top.api.base import RestApi


class TmallExchangeRefusereasonGetRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.dispute_id = None
        self.dispute_type = None
        self.fields = None

    def getapiname(self):
        return 'tmall.exchange.refusereason.get'
