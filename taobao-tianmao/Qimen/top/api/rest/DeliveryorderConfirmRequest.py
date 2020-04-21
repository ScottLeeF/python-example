'''
Created by auto_sdk on 2018.08.16
'''
from top.api.base import RestApi


class DeliveryorderConfirmRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.deliveryOrder = None
        self.extendProps = None
        self.orderLines = None
        self.packages = None

    def getapiname(self):
        return 'taobao.qimen.deliveryorder.confirm'
