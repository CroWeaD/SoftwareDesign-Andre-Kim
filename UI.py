import ManageDelivery

class UI:
    def __init__(self):
        self.result = []
        
    def showResult(self):
        print("This is UI class")

class RequestDeliveryUI(UI):
    def __init__(self, data):
        self.orderInfo = data 
        
    def showResult(self):
        print("_showResult()")
        
        print("--------------------------")
        print("request success...")
        print("courier name\t:", self.result[0])
        print("tracking number\t:", self.result[1])
        print("contract code\t:", self.result[2])
        print("--------------------------")
    
    def sendinformation(self):
        print("_sendinformation()")
        md = ManageDelivery.ManageDelivery()
        md.addInformation(0, self.orderInfo)
        md.transferOrderInformation()
        md.addInformation(1, md.couierInfo)
        self.result = md.transferCourierInformation()
        
        