'''
Created by auto_sdk on 2018.08.16
'''
from top.api.base import RestApi


class DeliveryorderCreateRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.deliveryOrder = None
        self.extendProps = None
        self.items = None
        self.orderLines = None

    def getapiname(self):
        return 'taobao.qimen.deliveryorder.create'
