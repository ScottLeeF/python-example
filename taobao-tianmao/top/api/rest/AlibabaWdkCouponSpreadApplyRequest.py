'''
Created by auto_sdk on 2019.10.15
'''
from top.api.base import RestApi


class AlibabaWdkCouponSpreadApplyRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.param_wdk_coupon_apply_param = None

    def getapiname(self):
        return 'alibaba.wdk.coupon.spread.apply'
