'''
Created by auto_sdk on 2018.08.16
'''
from top.api.base import RestApi


class ReturnorderConfirmRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.extendProps = None
        self.orderLines = None
        self.returnOrder = None

    def getapiname(self):
        return 'taobao.qimen.returnorder.confirm'
