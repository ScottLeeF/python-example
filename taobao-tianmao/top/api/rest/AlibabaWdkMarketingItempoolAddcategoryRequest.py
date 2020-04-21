'''
Created by auto_sdk on 2018.12.27
'''
from top.api.base import RestApi


class AlibabaWdkMarketingItempoolAddcategoryRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.common_activity_param = None
        self.item_pool_activity_category = None

    def getapiname(self):
        return 'alibaba.wdk.marketing.itempool.addcategory'
