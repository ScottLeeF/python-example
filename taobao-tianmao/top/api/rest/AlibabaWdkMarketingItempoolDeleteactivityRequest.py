'''
Created by auto_sdk on 2019.08.01
'''
from top.api.base import RestApi


class AlibabaWdkMarketingItempoolDeleteactivityRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.param = None

    def getapiname(self):
        return 'alibaba.wdk.marketing.itempool.deleteactivity'
