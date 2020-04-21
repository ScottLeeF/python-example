'''
Created by auto_sdk on 2018.08.09
'''
from top.api.base import RestApi


class TmallExchangeAgreeRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.address_id = None
        self.complete_address = None
        self.dispute_id = None
        self.fields = None
        self.leave_message = None
        self.leave_message_pics = None
        self.mobile = None
        self.post = None

    def getapiname(self):
        return 'tmall.exchange.agree'

    def getMultipartParas(self):
        return ['leave_message_pics']
