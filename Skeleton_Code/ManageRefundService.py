import Data_Storage
import CourierInfo
import CustomerCompanyInfo

class ManageRefundService:
    def __init__(self):
        self.refundInfo = []
    
    def sendRefundInformation(self):
        cc = CustomerCompanyInfo.CustomerCompanyInfo()
        cc.showRefundInformation()
        return
    
    def requestRefundService(self):
        ci = CourierInfo.CourierInfo([])
        ci.requestRetrieve()
        ci.sendCourierInformation()
    
    def addinformation(self):
        Data_Storage.DataStorage.insert([])
        
    def transferTrackingInformation(self):
        return self.refundInfo
          
            
            
