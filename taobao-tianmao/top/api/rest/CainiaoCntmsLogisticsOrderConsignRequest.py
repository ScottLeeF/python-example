'''
Created by auto_sdk on 2020.02.17
'''
from top.api.base import RestApi


class CainiaoCntmsLogisticsOrderConsignRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.content = None

    def getapiname(self):
        return 'cainiao.cntms.logistics.order.consign'
