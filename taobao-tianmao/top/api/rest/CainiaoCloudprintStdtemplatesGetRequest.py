'''
Created by auto_sdk on 2019.01.08
'''
from top.api.base import RestApi


class CainiaoCloudprintStdtemplatesGetRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)

    def getapiname(self):
        return 'cainiao.cloudprint.stdtemplates.get'
