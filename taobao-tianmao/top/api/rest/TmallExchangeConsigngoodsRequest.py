'''
Created by auto_sdk on 2018.08.09
'''
from top.api.base import RestApi


class TmallExchangeConsigngoodsRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.dispute_id = None
        self.fields = None
        self.logistics_company_name = None
        self.logistics_no = None
        self.logistics_type = None

    def getapiname(self):
        return 'tmall.exchange.consigngoods'
