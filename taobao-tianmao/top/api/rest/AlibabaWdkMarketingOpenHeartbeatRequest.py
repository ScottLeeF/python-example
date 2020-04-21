'''
Created by auto_sdk on 2019.03.26
'''
from top.api.base import RestApi


class AlibabaWdkMarketingOpenHeartbeatRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.heart_beat = None

    def getapiname(self):
        return 'alibaba.wdk.marketing.open.heartbeat'
