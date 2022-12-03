import os
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
    
    def showresult(self):
        #os.system("clear")
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
    
    def showresult(self):
        return super().showresult()
    
    def signUp(self):
        O1 = ManageSignUp.ManageSignUp([self.id, self.passwd, self.phonenum, self.add])
        self.result = O1.validateSignUp()

class SignInUI(ClientUI):
    def __init__(self):
        id = input("ID<The default id is 'kdi'>: ")      
        passwd = input("passwd<the default password is '1234'>: ")
        
        self.id = id
        self.passwd = passwd
    
    def showresult(self):
        return super().showresult()
    
    def signIn(self):
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
    
    def showresult(self):
        return super().showresult()
    
    def sendProfile(self, user):
        O1 = ManageProfile.ManageProfile([self.passwd, self.phonenum, self.add])
        self.result = O1.updateProfile(user)
     
class TrackingServiceUI(ClientUI):   
    
    def __init__(self):
        self.trackingInfo = []
    
    def showresult(self):
        return super().showresult()
    
    def sendTrackingRequest(self):
        O1 = ManageTracking.ManageTracking()
        O1.requestTrackingService()
        O1.addinformation()
        self.result = O1.transferTrackingInformation()
       
class SendingServiceUI(ClientUI):   
    
    def __init__(self):
        self.sendingInfo = []
    
    def showresult(self):
        return super().showresult()
    
    def sendSendingRequest(self):
        O1 = ManageSendService.ManageSendService()
        O1.requestSendingService()
        O1.addinformation()
        O1.requestTrackingInfo()
        
        while True:
            break
        
        O1.transferTrackingInformation()
        self.result = []
        
           
class RefundServiceUI(ClientUI):   
    
    def __init__(self):
        self.refundInfo = []
    
    def showresult(self):
        return super().showresult()
    
    def sendRefundRequest(self):
        O1 = ManageRefundService.ManageRefundService()
        O1.sendRefundInformation()
        O1.requestRefundService()
        O1.addinformation()
        self.result = O1.transferTrackingInformation()                