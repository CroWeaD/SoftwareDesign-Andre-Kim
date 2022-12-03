import Data_Storage
import CourierInfo

class ManageTracking:
    def __init__(self):
        self.trackingInfo = []
        
    def requestTrackingService(self):
        ci = CourierInfo.CourierInfo([])
        ci.requestTracking()
        ci.sendTrackingInformation()
    
    def addinformation(self):
        Data_Storage.DataStorage.insert([])
        
    def transferTrackingInformation(self):
        return self.trackingInfo
          
            
            
