import Data_Storage
import CourierInfo

class ManageDelivery:
    def __init__(self):
        self.orderinfo = []
        self.couierInfo = []
        
    def addInformation(self, mode, list):
        if mode == 0:
            self.orderinfo = list
            Data_Storage.DataStorage.orderInfo.append(list)
            Data_Storage.DataStorage.insert(list)
        elif mode == 1:
            Data_Storage.DataStorage.courierInfo.append(list)
            Data_Storage.DataStorage.insert(list)
    
    def transferOrderInformation(self):
        ci = CourierInfo.CourierInfo(self.orderinfo)
        ci.sendOrderInformation()
        self.couierInfo = ci.sendCourierInformation()
        
    def transferCourierInformation(self):
        return self.couierInfo
          
            
            
