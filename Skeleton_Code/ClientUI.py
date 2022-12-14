import os
import time
import UI
import CourierInfo
import CustomerCompanyInfo
import ManageSignUp
import ManageSignIn
import ManageProfile
import ManageTracking
import ManageSendService
import ManageRefundService


class ClientUI(UI.UI):
    
    def showResult(self):
        #os.system("clear")
        print("_showResult()")
        print("--------------------------")
        print(self.result)
        print("--------------------------")
        
class SignUpUI(ClientUI):
    def __init__(self):
        id = input("ID: ")  
        passwd = input("passwd: ")
        phonenum = input("phonenum (ex - 010-1234-5678): ")
        add = input("address: ")
        
        self.id = id
        self.passwd = passwd
        self.phonenum = phonenum
        self.add = add
    
    def signUp(self):
        print("_signUp()")
        O1 = ManageSignUp.ManageSignUp([self.id, self.passwd, self.phonenum, self.add])
        self.result = O1.validateSignUp()

class SignInUI(ClientUI):
    def __init__(self, id, passwd):
        
        if(id == ""):
            self.id = input("ID<The default id is 'root'>: ")
        else:
            self.id = id
            
        if(passwd == ""):
            self.passwd = input("passwd<the default password is '1234'>: ")
        else:
            self.passwd = passwd
    
    def signIn(self):
        print("_signIn()")
        O1 = ManageSignIn.ManageSignIn([self.id, self.passwd])
        self.result = O1.validateSignIn()

class UpdateProfileUI(ClientUI):
    def __init__(self):
        passwd = input("passwd: ")
        phonenum = input("phonenum (ex - 010-1234-5678): ")
        add = input("address: ")
        
        self.passwd = passwd
        self.phonenum = phonenum
        self.add = add
    
    def sendProfile(self, user):
        print("_sendProfile()")
        O1 = ManageProfile.ManageProfile([self.passwd, self.phonenum, self.add])
        self.result = O1.updateProfile(user)
        print("_result")
     
class TrackingServiceUI(ClientUI):   
    
    def __init__(self):
        self.trackingInfo = []
    
    def showResult(self):
        print("_showResult()")
        print(">>", self.result)
    
    def sendTrackingRequest(self):
        print("_sendTrackingRequest()")
        O1 = ManageTracking.ManageTracking()
        O1.requestTrackingService()
        O1.addInformation(O1.trackingInfo)
        self.result = O1.transferTrackingInformation()
       
class SendingServiceUI(ClientUI):   
    
    def __init__(self, data):
        self.sendingInfo = data
    
    def sendSendingRequest(self):
        print("_sendSendingRequest()")
        O1 = ManageSendService.ManageSendService()
        O1.addInformation(0, self.sendingInfo)
        O1.requestSendingService()
        print(O1.courierInfo)
        O1.addInformation(1, O1.courierInfo)
        O1.requestTrackingInfo()
        O1.addInformation(2, O1.trackingInfo)
        self.result = O1.transferTrackingInformation()
        
        
           
class RefundServiceUI(ClientUI):   
    
    def __init__(self):
        self.refundInfo = []
    
    def sendRefundRequest(self):
        print("_sendRefundRequest()")
        O1 = ManageRefundService.ManageRefundService()
        O1.sendRefundInformation()
        O1.requestRefundService()
        O1.addInformation(1, O1.courierInfo)
        O1.requestTrackingInfo()
        O1.addInformation(2, O1.trackingInfo)
        self.result = O1.transferTrackingInformation()                