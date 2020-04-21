'''
Created by auto_sdk on 2018.07.26
'''
from top.api.base import RestApi


class AlibabaTianjiDistributorOrderSubmitRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.item_serial_no = None
        self.order_no = None
        self.product_serial_no = None

    def getapiname(self):
        return 'alibaba.tianji.distributor.order.submit'
