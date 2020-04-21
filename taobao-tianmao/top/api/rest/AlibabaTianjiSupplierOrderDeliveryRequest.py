'''
Created by auto_sdk on 2018.07.26
'''
from top.api.base import RestApi


class AlibabaTianjiSupplierOrderDeliveryRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.param_distribution_order_logistics_model = None

    def getapiname(self):
        return 'alibaba.tianji.supplier.order.delivery'
