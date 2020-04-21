'''
Created by auto_sdk on 2019.11.20
'''
from top.api.base import RestApi


class SupplierSynchronizeRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.actionType = None
        self.area = None
        self.city = None
        self.countryCode = None
        self.detailAddress = None
        self.email = None
        self.isValid = None
        self.name = None
        self.province = None
        self.remark = None
        self.supplierCode = None
        self.supplierName = None
        self.tel = None
        self.town = None

    def getapiname(self):
        return 'taobao.qimen.supplier.synchronize'
