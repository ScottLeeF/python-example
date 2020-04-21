'''
Created by auto_sdk on 2019.03.04
'''
from top.api.base import RestApi


class AlibabaWdkMarketingOpenVersionCountRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.operate_id = None
        self.version_id = None

    def getapiname(self):
        return 'alibaba.wdk.marketing.open.version.count'
