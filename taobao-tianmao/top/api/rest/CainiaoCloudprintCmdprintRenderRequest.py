'''
Created by auto_sdk on 2019.02.20
'''
from top.api.base import RestApi


class CainiaoCloudprintCmdprintRenderRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.params = None

    def getapiname(self):
        return 'cainiao.cloudprint.cmdprint.render'
