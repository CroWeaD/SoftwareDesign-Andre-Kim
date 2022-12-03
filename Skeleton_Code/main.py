import os
import time
import UI
import ClientUI

data1 = [["11ST_1234", "010-1234-5678", "Cost", "Address"]]
data2 = (("CU1234", "010-5678-9087", "Address", "Cost"))
data3 = ()
data4 = ()

def startscreen():
    os.system("clear")
    print("------------------------------")
    print("Select mode")
    print("1. login")
    print("2. make profile")
    print("------------------------------")
    mode = int(input(">> "))
    os.system("clear")
    
    return mode

def menu():
    os.system("clear")
    print("------------------------------")
    print("1. Update Profile")
    print("2. Track on a package")
    print("3. Send a package")
    print("4. Refund a package")
    print("0. QUIT")
    print("------------------------------")
    mode = int(input(">> "))
    os.system("clear")
    
    return mode

def main():
    while True:
        
        mode = startscreen()
        
        if mode == 1:
            os.system("clear")
            si = ClientUI.SignInUI()
            si.signIn()
            
            si.showresult()
            time.sleep(3)
            if si.result == True:
                break
            else:
                continue
            
        
        elif mode == 2:
            os.system("clear")
            su = ClientUI.SignUpUI()
            su.signUp()
            su.showresult()
            time.sleep(5)
        
        else:
            continue
        
    while True:
        mode = menu()
        
        if mode == 0:
            print("Exit!")
            break
        
        elif mode == 1:
            up = ClientUI.UpdateProfileUI()
            up.sendProfile([si.id])
            up.showresult()
            time.sleep(5)
        
        elif mode == 2:
            rd = UI.RequestDeliveryUI(data1[0])
            rd.sendinformation()
            rd.showresult()
            time.sleep(3)
            
            ts = ClientUI.TrackingServiceUI()
            ts.sendTrackingRequest()
            ts.showresult()
            time.sleep(3)
            
        elif mode == 3:
            ss = ClientUI.SendingServiceUI()
            ss.sendSendingRequest()
            ss.showresult()
            time.sleep(3)
                
        elif mode == 4:
            sr = ClientUI.RefundServiceUI()
            sr.sendRefundRequest()
            sr.showresult()
            time.sleep(3)
           
        else:
            continue
          
    
    
    


#main function
if __name__ == "__main__":
    main()