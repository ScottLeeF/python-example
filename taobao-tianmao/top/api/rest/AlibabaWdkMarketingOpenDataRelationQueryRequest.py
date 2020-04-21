'''
Created by auto_sdk on 2019.03.04
'''
from top.api.base import RestApi


class AlibabaWdkMarketingOpenDataRelationQueryRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.biz_code = None
        self.out_data_ids = None
        self.sub_biz_code = None

    def getapiname(self):
        return 'alibaba.wdk.marketing.open.data.relation.query'
