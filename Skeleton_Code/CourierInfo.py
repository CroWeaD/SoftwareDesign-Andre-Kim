class CourierInfo:
    def __init__(self):
        self.courierInfo = []
        
    def sendOrderInformation(self):
        print("_sendOrderInformation() (CourierInfo --> courier)")
        print("_send a tracking number and contract code(courier --> CorierInfo)")
        print("======================================")
        print("ex)")
        print("corier name \t: 11ST_1234")
        print("tracking number : EG033025977JA")
        print("contract code \t: 3-17")
        print("======================================")
        self.courierInfo = ["11ST_1234","EG033025977JA", "3-17"]
        return
    
    def sendCourierInformation(self):
        print("_sendCourirerInformation()")
        
    def requestTracking(self):
        print("_requestTracking()(CourierInfo --> courier)")
        print("_tracking information(corier --> CorierInfo)")
        return ["hub_1", "hub_2", "hub_3"]
        
    def sendTrackingInformation(self):
        print("_sendTrackingInformation()")
        return
    
    def requestSending(self):
        print("_requestSending (CourierInfo --> courier)")
        print("_send a tracking number and contract code(courier --> CorierInfo)")
        print("======================================")
        print("ex)")
        print("corier name \t: CU_5935")
        print("tracking number : HG032632975JB")
        print("contract code \t: 5-34")
        print("======================================")
        self.courierInfo = ["CU_5935","HG032632975JB", "5-34"]
        return
    
    def requestRetrieve(self):
        print("_requestRetrieve() (CorierInfo --> corier)")
        print("_send a tracking number and contract code(courier --> CorierInfo)")
        print("======================================")
        print("ex)")
        print("corier name \t: CU_5935")
        print("tracking number : HG032632975JB")
        print("contract code \t: 5-34")
        print("======================================")
        self.courierInfo = ["CJ_A382", "ID930285739BI", "8-26"]
        