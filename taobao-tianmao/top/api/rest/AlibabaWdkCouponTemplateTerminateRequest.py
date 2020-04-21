'''
Created by auto_sdk on 2019.10.15
'''
from top.api.base import RestApi


class AlibabaWdkCouponTemplateTerminateRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.param_coupon_template_terminate_request = None

    def getapiname(self):
        return 'alibaba.wdk.coupon.template.terminate'
