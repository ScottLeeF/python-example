'''
Created by auto_sdk on 2018.07.25
'''
from top.api.base import RestApi


class AlibabaAlitjOrderRealnamecardInfoSubmitRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.iccid = None
        self.order_no = None

    def getapiname(self):
        return 'alibaba.alitj.order.realnamecard.info.submit'
