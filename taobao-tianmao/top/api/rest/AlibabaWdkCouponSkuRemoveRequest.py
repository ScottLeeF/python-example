'''
Created by auto_sdk on 2019.10.15
'''
from top.api.base import RestApi


class AlibabaWdkCouponSkuRemoveRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.param_coupon_template_item_request = None

    def getapiname(self):
        return 'alibaba.wdk.coupon.sku.remove'
