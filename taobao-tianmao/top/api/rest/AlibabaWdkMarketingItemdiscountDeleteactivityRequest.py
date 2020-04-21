'''
Created by auto_sdk on 2019.04.12
'''
from top.api.base import RestApi


class AlibabaWdkMarketingItemdiscountDeleteactivityRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.param = None

    def getapiname(self):
        return 'alibaba.wdk.marketing.itemdiscount.deleteactivity'
