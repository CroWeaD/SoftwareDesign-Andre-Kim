import Data_Storage
import CourierInfo

class ManageDelivery:
    def __init__(self):
        self.orderinfo = []
        self.couierInfo = []
        
    def addInformation(self, mode, list):
        if mode == 0:
            print("_addInformation() (order information)")
            Data_Storage.DataStorage.orderInfo.extend(list)
            Data_Storage.DataStorage.insert(list)
        elif mode == 1:
            print("_addInformation() (courier information)")
            Data_Storage.DataStorage.courierInfo.extend(list)
            Data_Storage.DataStorage.insert(list)
    
    def transferOrderInformation(self):
        print("_transferOrderInformation()")
        print("======================================")
        print("order number\t:", Data_Storage.DataStorage.orderInfo[0])
        print("package name\t:", Data_Storage.DataStorage.orderInfo[1])
        print("cost\t\t:", Data_Storage.DataStorage.orderInfo[2])
        print("client name\t:", Data_Storage.DataStorage.orderInfo[3])
        print("receiver\t:", Data_Storage.DataStorage.orderInfo[4])
        print("arrive point\t:", Data_Storage.DataStorage.orderInfo[5])
        print("phone number\t:", Data_Storage.DataStorage.orderInfo[6])
        print("message\t\t:", Data_Storage.DataStorage.orderInfo[7])
        print("payment Type\t:", Data_Storage.DataStorage.orderInfo[8])
        print("sender\t\t:", Data_Storage.DataStorage.orderInfo[9])
        print("start point\t:", Data_Storage.DataStorage.orderInfo[10])
        print("======================================")
        ci = CourierInfo.CourierInfo()
        ci.sendOrderInformation()
        ci.sendCourierInformation()
        self.couierInfo = ci.courierInfo
        
        
    def transferCourierInformation(self):
        print("_transferCourierInformation()")
        print("======================================")
        print("Data_Storage")
        print("orderInfo\t:", Data_Storage.DataStorage.orderInfo)
        print("courierInfo\t:", Data_Storage.DataStorage.courierInfo)
        print("======================================")
        return Data_Storage.DataStorage.courierInfo
          
            
            
