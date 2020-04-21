'''
Created by auto_sdk on 2019.04.12
'''
from top.api.base import RestApi


class AlibabaWdkMarketingItemdiscountAdditemRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.param0 = None
        self.param1 = None

    def getapiname(self):
        return 'alibaba.wdk.marketing.itemdiscount.additem'
