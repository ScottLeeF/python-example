'''
Created by auto_sdk on 2019.07.31
'''
from top.api.base import RestApi


class AlibabaWdkMarketingOpenDarunfaActivitySkuSyncRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.activity_id = None
        self.activity_sku_list = None
        self.shop_id = None
        self.version_id = None

    def getapiname(self):
        return 'alibaba.wdk.marketing.open.darunfa.activity.sku.sync'
