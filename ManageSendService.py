import Data_Storage
import CourierInfo
import time

class ManageSendService:
    def __init__(self):
        self.sendingInfo = []
        self.courierInfo = []
        self.trackingInfo = []
        
    def requestSendingService(self):
        print("_requestSendingService()")
        print("======================================")
        print("order number\t:", Data_Storage.DataStorage.sendingInfo[0])
        print("package name\t:", Data_Storage.DataStorage.sendingInfo[1])
        print("cost\t\t:", Data_Storage.DataStorage.sendingInfo[2])
        print("sender\t\t:", Data_Storage.DataStorage.sendingInfo[3])
        print("phone number\t:", Data_Storage.DataStorage.sendingInfo[4])
        print("start point\t:", Data_Storage.DataStorage.sendingInfo[5])
        print("receiver\t:", Data_Storage.DataStorage.sendingInfo[6])
        print("phone number\t:", Data_Storage.DataStorage.sendingInfo[7])
        print("arrive point\t:", Data_Storage.DataStorage.sendingInfo[8]) 
        print("package type\t:", Data_Storage.DataStorage.sendingInfo[9]) 
        print("payment type\t:", Data_Storage.DataStorage.sendingInfo[10])
        print("======================================")
        ci = CourierInfo.CourierInfo()
        ci.requestSending()
        ci.sendCourierInformation()
        self.courierInfo = ci.courierInfo
    
    def addInformation(self, mode, list):
        if mode == 0:
            print("_addInformation() (sending information)")
            Data_Storage.DataStorage.sendingInfo = (list)
            Data_Storage.DataStorage.insert(list)
        elif mode == 1:
            print("_addInformation() (courier information)")
            Data_Storage.DataStorage.courierInfo = list
            Data_Storage.DataStorage.insert(list)
        elif mode == 2:
            print("_addInformation() (tracking information)")
            Data_Storage.DataStorage.trackingInfo = list
            Data_Storage.DataStorage.insert(list)
        
    def transferTrackingInformation(self):
        print("_transferTrackingInformation()")
        print("======================================")
        print("Data_Storage")
        print("sendingInfo\t:", Data_Storage.DataStorage.sendingInfo)
        print("courierInfo\t:", Data_Storage.DataStorage.courierInfo)
        print("trackingInfo\t:", Data_Storage.DataStorage.trackingInfo)
        print("======================================")
        return Data_Storage.DataStorage.trackingInfo
          
    def requestTrackingInfo(self):
        print("_requestTrackingInfo()")
        ci = CourierInfo.CourierInfo()
        self.trackingInfo.extend([Data_Storage.DataStorage.sendingInfo[5]])
        self.trackingInfo.extend(ci.requestTracking())
        self.trackingInfo.extend([Data_Storage.DataStorage.sendingInfo[8]])
        for i in range(0, len(self.trackingInfo)) :
            ci.sendTrackingInformation()
            print(self.trackingInfo[i])
            time.sleep(1)
