'''
Created by auto_sdk on 2019.10.18
'''
from top.api.base import RestApi


class AlibabaWdkMarketingOpenDarunfaActivitySyncRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.activity_list = None
        self.shop_id = None
        self.version_id = None

    def getapiname(self):
        return 'alibaba.wdk.marketing.open.darunfa.activity.sync'
