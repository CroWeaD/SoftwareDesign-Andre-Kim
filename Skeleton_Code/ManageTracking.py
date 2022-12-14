import Data_Storage
import CourierInfo
import time

class ManageTracking:
    def __init__(self):
        self.trackingInfo = []

        
    def requestTrackingService(self):
        print("_requestTrackingService()")
        ci = CourierInfo.CourierInfo()
        self.trackingInfo.extend([Data_Storage.DataStorage.orderInfo[10]])
        self.trackingInfo.extend(ci.requestTracking())
        self.trackingInfo.extend([Data_Storage.DataStorage.orderInfo[5]])
        for i in range(0, len(self.trackingInfo)) :
            ci.sendTrackingInformation()
            print(self.trackingInfo[i])
            time.sleep(1)

    
    def addInformation(self, list):
        print("_addInforamtion() (tracking information)")
        Data_Storage.DataStorage.trackingInfo = list
        Data_Storage.DataStorage.insert(list)
        
    def transferTrackingInformation(self):
        print("_transferTrackingInformation()")
        print("======================================")
        print("Data_Storage")
        print("trackingInfo\t:", Data_Storage.DataStorage.trackingInfo)
        print("======================================")
        return Data_Storage.DataStorage.trackingInfo
          
            
            
