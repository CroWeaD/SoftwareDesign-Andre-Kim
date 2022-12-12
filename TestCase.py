import unittest
import ClientUI
import UI


# TestCase를 작성
class ProfileTests(unittest.TestCase): 

    def test_case1(self):
        print("<< use-case 1 : Sign up >>")
        print("_request sign-up")
        su = ClientUI.SignUpUI()
        su.signUp()
        su.showResult()
        
    def test_case2(self):
        print("<< use-case 2 : sign in >>")
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
        print("<< use-case 3 : Update a profile >>")
        print("_update a profile")
        up = ClientUI.UpdateProfileUI()
        up.sendProfile(["root"])
        up.showResult()
        
    def test_case5(self):
        print("<< use-case 5 : track a package >>")
        print("_request a tracking information")
        ts = ClientUI.TrackingServiceUI()
        ts.sendTrackingRequest()
        ts.showResult()
    
    def test_case6(self):
        print("<< use-case 6 : send a package >>")
        print("_request send a package")
        ss = ClientUI.SendingServiceUI()
        ss.sendSendingRequest()
        ss.showResult()
    
    def test_case7(self):
        print("<< use-case 7 : Refund a package >>")
        print("_request refund service")
        sr = ClientUI.RefundServiceUI()
        sr.sendRefundRequest()
        sr.showResult()
    
class CCTest(unittest.TestCase):
    
    def test_case4(self):
        data1 = ["11ST_1234", "010-1234-5678", "Cost", "Address"]
        print("<< use-case 4 : request delivery >>")
        print("_Reqeust a delivery service")
        rd = UI.RequestDeliveryUI(data1)
        rd.sendinformation()
        rd.showResult()
        

# unittest를 실행
if __name__ == '__main__':  
    unittest.main()