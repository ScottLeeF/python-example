'''
Created by auto_sdk on 2018.07.25
'''
from top.api.base import RestApi


class FenxiaoProductImportFromAuctionRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.auction_id = None
        self.product_line_id = None
        self.trade_type = None

    def getapiname(self):
        return 'taobao.fenxiao.product.import.from.auction'
