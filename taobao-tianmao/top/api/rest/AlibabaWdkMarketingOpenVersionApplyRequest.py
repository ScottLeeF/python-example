'''
Created by auto_sdk on 2019.04.16
'''
from top.api.base import RestApi


class AlibabaWdkMarketingOpenVersionApplyRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.sync_version = None

    def getapiname(self):
        return 'alibaba.wdk.marketing.open.version.apply'
