'''
Created by auto_sdk on 2019.10.15
'''
from top.api.base import RestApi


class AlibabaWdkCouponTemplateCreateRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.param_coupon_template_operate_request = None

    def getapiname(self):
        return 'alibaba.wdk.coupon.template.create'
