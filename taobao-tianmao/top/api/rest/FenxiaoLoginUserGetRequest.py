'''
Created by auto_sdk on 2018.11.10
'''
from top.api.base import RestApi


class FenxiaoLoginUserGetRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)

    def getapiname(self):
        return 'taobao.fenxiao.login.user.get'
