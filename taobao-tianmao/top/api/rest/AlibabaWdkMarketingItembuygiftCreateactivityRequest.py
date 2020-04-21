'''
Created by auto_sdk on 2018.11.16
'''
from top.api.base import RestApi


class AlibabaWdkMarketingItembuygiftCreateactivityRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.param = None

    def getapiname(self):
        return 'alibaba.wdk.marketing.itembuygift.createactivity'
