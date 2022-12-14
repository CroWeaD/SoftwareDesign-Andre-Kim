import Data_Storage
import CourierInfo
import CustomerCompanyInfo
import time

class ManageRefundService:
    def __init__(self):
        self.refundInfo = []
        self.courierInfo = []
        self.trackingInfo = []
    
    def sendRefundInformation(self):
        print("_sendRefundInformation()")
        cc = CustomerCompanyInfo.CustomerCompanyInfo()
        cc.showRefundInformation()
        return
    
    def requestRefundService(self):
        print("_requestRefundService()")
        ci = CourierInfo.CourierInfo()
        ci.requestRetrieve()
        ci.sendCourierInformation()
    
    def addInformation(self, mode, list):
        if mode == 1:
            print("_addInformation() (courier information)")
            Data_Storage.DataStorage.courierInfo.extend(list)
            Data_Storage.DataStorage.insert(list)
        elif mode == 2:
            print("_addInformation() (tracking information)")
            Data_Storage.DataStorage.trackingInfo.extend(list)
            Data_Storage.DataStorage.insert(list)
        
    def transferTrackingInformation(self):
        print("_transferTrackingInformation()")
        print("======================================")
        print("Data_Storage")
        print("courierInfo\t:", Data_Storage.DataStorage.courierInfo)
        print("TrackingInfo\t:", Data_Storage.DataStorage.trackingInfo)
        print("======================================")
        return Data_Storage.DataStorage.trackingInfo
          
    def requestTrackingInfo(self):
        print("_requestTrackingInfo()")
        ci = CourierInfo.CourierInfo()
        self.trackingInfo.extend([Data_Storage.DataStorage.orderInfo[5]])
        self.trackingInfo.extend(reversed(ci.requestTracking()))
        self.trackingInfo.extend([Data_Storage.DataStorage.orderInfo[10]])
        for i in range(0, len(self.trackingInfo)) :
            ci.sendTrackingInformation()
            print(self.trackingInfo[i])
            time.sleep(1)

