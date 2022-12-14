import ManageDelivery

class UI:
    def __init__(self):
        self.result = []
        
    def showResult(self):
        print("--------------------------")
        print("request success...")
        print(self.result)
        print("--------------------------")

class RequestDeliveryUI(UI):
    def __init__(self, data):
        self.orderInfo = data 
        
    def showResult(self):
        print("_showResult()")
        super().showResult()
    
    def sendinformation(self):
        print("_sendinformation()")
        md = ManageDelivery.ManageDelivery()
        md.addInformation(0, self.orderInfo)
        md.transferOrderInformation()
        md.addInformation(1, md.couierInfo)
        self.result = md.transferCourierInformation()
        
        