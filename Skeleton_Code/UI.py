import ManageDelivery

class UI:
    def __init__(self):
        self.result = []
        
    def showresult(self):
        print("This is UI class")

class RequestDeliveryUI(UI):
    def __init__(self, data):
        self.orderInfo = data 
        
    def showresult(self):
        print("--------------------------")
        print(self.result)
        print("--------------------------")
    
    def sendinformation(self):
        md = ManageDelivery.ManageDelivery()
        md.addInformation(0, self.orderInfo)
        md.transferOrderInformation()
        md.addInformation(1, md.couierInfo)
        self.result = md.transferCourierInformation()
        
        
        