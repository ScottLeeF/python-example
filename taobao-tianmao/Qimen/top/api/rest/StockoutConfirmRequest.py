'''
Created by auto_sdk on 2020.03.03
'''
from top.api.base import RestApi


class StockoutConfirmRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.deliveryOrder = None
        self.extendProps = None
        self.orderLines = None
        self.packages = None

    def getapiname(self):
        return 'taobao.qimen.stockout.confirm'
