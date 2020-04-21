'''
Created by auto_sdk on 2018.07.25
'''
from top.api.base import RestApi


class TmallChannelProductsGetRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.top_query_product_d_o = None

    def getapiname(self):
        return 'tmall.channel.products.get'
