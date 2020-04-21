'''
Created by auto_sdk on 2018.07.25
'''
from top.api.base import RestApi


class FenxiaoTradePrepayOfflineAddRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.offline_add_prepay_param = None

    def getapiname(self):
        return 'taobao.fenxiao.trade.prepay.offline.add'
