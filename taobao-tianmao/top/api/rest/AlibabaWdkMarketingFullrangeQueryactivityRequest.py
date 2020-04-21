'''
Created by auto_sdk on 2018.08.23
'''
from top.api.base import RestApi


class AlibabaWdkMarketingFullrangeQueryactivityRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.param0 = None

    def getapiname(self):
        return 'alibaba.wdk.marketing.fullrange.queryactivity'
