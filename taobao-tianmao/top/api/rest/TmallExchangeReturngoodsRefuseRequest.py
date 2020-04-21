'''
Created by auto_sdk on 2018.07.25
'''
from top.api.base import RestApi


class TmallExchangeReturngoodsRefuseRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.dispute_id = None
        self.leave_message = None
        self.leave_message_pics = None
        self.seller_refuse_reason_id = None

    def getapiname(self):
        return 'tmall.exchange.returngoods.refuse'

    def getMultipartParas(self):
        return ['leave_message_pics']
