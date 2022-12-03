import Data_Storage
import CourierInfo

class ManageSendService:
    def __init__(self):
        self.sendingInfo = []
        
    def requestSendingService(self):
        ci = CourierInfo.CourierInfo([])
        ci.requestSending()
        ci.sendCourierInformation()
    
    def addinformation(self):
        Data_Storage.DataStorage.insert([])
        
    def transferTrackingInformation(self):
        return self.sendingInfo
          
    def requestTrackingInfo(self):
        ci = CourierInfo.CourierInfo([])
        ci.sendTrackingInformation()
                
            
