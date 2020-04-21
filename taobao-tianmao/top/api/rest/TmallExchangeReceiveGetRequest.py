'''
Created by auto_sdk on 2018.08.09
'''
from top.api.base import RestApi


class TmallExchangeReceiveGetRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.biz_order_id = None
        self.buyer_id = None
        self.buyer_nick = None
        self.dispute_status_array = None
        self.end_created_time = None
        self.end_gmt_modifed_time = None
        self.fields = None
        self.logistic_no = None
        self.page_no = None
        self.page_size = None
        self.refund_id_array = None
        self.start_created_time = None
        self.start_gmt_modified_time = None

    def getapiname(self):
        return 'tmall.exchange.receive.get'
