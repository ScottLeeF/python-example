'''
Created by auto_sdk on 2018.07.25
'''
from top.api.base import RestApi


class CainiaoVmsServiceCollectvehiclerouteRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.col_date = None
        self.cp_code = None
        self.device_id = None
        self.latitude = None
        self.longitude = None
        self.vechile_number = None

    def getapiname(self):
        return 'cainiao.vms.service.collectvehicleroute'
