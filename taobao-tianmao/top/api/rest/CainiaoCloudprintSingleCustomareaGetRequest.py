'''
Created by auto_sdk on 2018.10.10
'''
from top.api.base import RestApi


class CainiaoCloudprintSingleCustomareaGetRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.seller_id = None

    def getapiname(self):
        return 'cainiao.cloudprint.single.customarea.get'
