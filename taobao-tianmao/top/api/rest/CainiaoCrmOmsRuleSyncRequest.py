'''
Created by auto_sdk on 2018.07.25
'''
from top.api.base import RestApi


class CainiaoCrmOmsRuleSyncRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.check_rule_msg = None
        self.is_auto_check = None
        self.is_open_cnauto = None
        self.is_sys_merge_order = None
        self.merge_order_cycle = None
        self.other_rule = None
        self.shop_code = None

    def getapiname(self):
        return 'cainiao.crm.oms.rule.sync'
