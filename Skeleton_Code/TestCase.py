import unittest
import ClientUI
import UI


# TestCase를 작성
class ProfileTests(unittest.TestCase): 

    def test_case1(self):
        print("<< test-case 1 : Sign up >>")
        print("_request sign-up")
        su = ClientUI.SignUpUI()
        su.signUp()
        su.showResult()
        
    def test_case2(self):
        print("<< test-case 2 : sign in >>")
        print("_request sign_in")
        si = ClientUI.SignInUI("", "")
        si.signIn()
        si.showResult()
        
class ClientTests(unittest.TestCase):
    
    def setUp(self):
        print("_request sign_in")
        si = ClientUI.SignInUI("root", "1234")
        si.signIn()
        si.showResult()
    
    def test_case3(self):
        print("<< test-case 3 : Update a profile >>")
        print("_update a profile")
        up = ClientUI.UpdateProfileUI()
        up.sendProfile(["root"])
        up.showResult()
        
    def test_case5(self):
        print("<< test-case 5 : track a package >>")
        
        data1 = ["20210325OXjG8", "I-pad_air_5", "750,000", "root", "Andre_Kim", "knu_IT-5_341", "010-1234-5678", "please_fast", "card", "APPLE", "California" ]
        print("_Reqeust a delivery service")
        rd = UI.RequestDeliveryUI(data1)
        rd.sendinformation()
        rd.showResult()
        print("_request a tracking information")
        ts = ClientUI.TrackingServiceUI()
        ts.sendTrackingRequest()
        ts.showResult()
    
    def test_case6(self):
        print("<< test-case 6 : send a package >>")
        #       send information example
        #       [0:order number, 1:package name, 2:cost, 3:send, 4:phone number, 5:start_point, 6:receiver, 7:phone number(rcv), 8:arrive_point, 9:package type, 10:payment type ]
        data2 = ["20210325OYDG3", "I-pad_pro", "100,000", "Andre_Lee", "010-1212-1212", "2_chung_dam", "Andre Park", "010-3434-3434", "knu_IT-5_341", "normal", "Cash on delivery"]
        print("_request send a package")
        ss = ClientUI.SendingServiceUI(data2)
        ss.sendSendingRequest()
        ss.showResult()
    
    def test_case7(self):
        print("<< test-case 7 : Refund a package >>")
        
        data1 = ["20210325OXjG8", "I-pad_air_5", "750,000", "root", "Andre_Kim", "knu_IT-5_341", "010-1234-5678", "please_fast", "card", "APPLE", "California" ]
        print("_Reqeust a delivery service")
        rd = UI.RequestDeliveryUI(data1)
        rd.sendinformation()
        rd.showResult()
        print("_request refund service")
        sr = ClientUI.RefundServiceUI()
        sr.sendRefundRequest()
        sr.showResult()
    
class CCTest(unittest.TestCase):
    
    def test_case4(self):
        #       order information example
        #       [0:order number, 1:package name, 2:cost, 3:client name, 4:receiver, 5:arrive_point, 6:phone number, 7:message, 8:payment type, 9:sender, 10:start_point ]
        data1 = ["20210325OXjG8", "I-pad_air_5", "750,000", "root", "Andre_Kim", "knu_IT-5_341", "010-1234-5678", "please_fast", "card", "APPLE", "California" ]
        print("<< use-case 4 : request delivery >>")
        print("_Reqeust a delivery service")
        rd = UI.RequestDeliveryUI(data1)
        rd.sendinformation()
        rd.showResult()
        

# unittest를 실행
if __name__ == '__main__':  
    unittest.main()