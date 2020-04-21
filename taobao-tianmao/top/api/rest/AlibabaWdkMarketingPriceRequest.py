'''
Created by auto_sdk on 2018.10.12
'''
from top.api.base import RestApi


class AlibabaWdkMarketingPriceRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.begin_time = None
        self.end_time = None
        self.page_index = None
        self.page_size = None
        self.shop_ids = None
        self.sku_codes = None

    def getapiname(self):
        return 'alibaba.wdk.marketing.price'
