'''
Created by auto_sdk on 2018.07.25
'''
from top.api.base import RestApi


class TmallChannelProductsQueryRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.page_num = None
        self.page_size = None
        self.product_ids = None
        self.product_line_id = None
        self.product_number = None
        self.sku_number = None

    def getapiname(self):
        return 'tmall.channel.products.query'
