'''
Created by auto_sdk on 2018.10.24
'''
from top.api.base import RestApi


class FenxiaoTradePrepayOfflineReduceRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.offline_reduce_prepay_param = None

    def getapiname(self):
        return 'taobao.fenxiao.trade.prepay.offline.reduce'
