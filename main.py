import os
import time
import UI
import ClientUI
#       order information example
#       [0:order number, 1:package name, 2:cost, 3:client name, 4:receiver, 5:arrive_point, 6:phone number, 7:message, 8:payment type, 9:sender, 10:start_point ]
data1 = ["20210325OXjG8", "I-pad_air_5", "750,000", "root", "Andre_Kim", "knu_IT-5_341", "010-1234-5678", "please_fast", "card", "APPLE", "California" ]

#       send information example
#       [0:order number, 1:package name, 2:cost, 3:send, 4:phone number, 5:start_point, 6:receiver, 7:phone number(rcv), 8:arrive_point, 9:package type, 10:payment type ]
data2 = ["20210325OYDG3", "I-pad_pro", "100,000", "Andre_Lee", "010-1212-1212", "2_chung_dam", "Andre Park", "010-3434-3434", "knu_IT-5_341", "normal", "Cash on delivery"]

def startscreen():
    #os.system("clear")
    print("------------------------------")
    print("Select mode")
    print("1. login")
    print("2. make profile")
    print("------------------------------")
    mode = int(input(">> "))
    #os.system("clear")
    
    return mode

def menu():
    #os.system("clear")
    print("------------------------------")
    print("1. Update Profile")
    print("2. Request a delivery")
    print("3. Track a package")
    print("4. Send a package")
    print("5. Refund a package")
    print("0. QUIT")
    print("------------------------------")
    mode = int(input(">> "))
    #os.system("clear")
    
    return mode

def main():
    while True:
        
        mode = startscreen()
        
        if mode == 1:
            #os.system('clear')
            print("<< use-case 2 : Sign in >>")
            print("_request sign_in")
            si = ClientUI.SignInUI("", "")
            si.signIn()
            si.showResult()
            #time.sleep(3)
            if si.result == True:
                break
            else:
                continue
            
        elif mode == 2:
            #os.system('clear')
            print("<< use-case 1 : Sign up >> ")
            print("_request sign-up")
            su = ClientUI.SignUpUI()
            su.signUp()
            su.showResult()
            #time.sleep(5)
        
        else:
            continue
        
    chance = 0
    while True:
        mode = menu()
        
        if mode == 0:
            print("Exit!")
            break
        
        elif mode == 1:
            print("<< use-case 3 : Update a profile")
            print("_update a profile")
            up = ClientUI.UpdateProfileUI()
            up.sendProfile([si.id])
            up.showResult()
            #time.sleep(5)
        
        elif mode == 2:
            print("<< use-case 4 : request delivery >>")
            print("_Reqeust a delivery service")
            rd = UI.RequestDeliveryUI(data1)
            rd.sendinformation()
            rd.showResult()
            chance = 1
            #time.sleep(3)
            
        elif mode == 3:
            if (not chance) :
                print("use-case 2 is pre condition")
                print("please request delivery first")
                continue
            print("<< use-case 5 : track a package >>")
            print("_request a trackin information")
            ts = ClientUI.TrackingServiceUI()
            ts.sendTrackingRequest()
            ts.showResult()
            #time.sleep(3)
            
        elif mode == 4:
            print("<< use-case 6 : send a package >>")
            print("_request send a package")
            ss = ClientUI.SendingServiceUI(data2)
            ss.sendSendingRequest()
            ss.showResult()
            #time.sleep(3)
                
        elif mode == 5:
            if (not chance) :
                print("use-case 2 is pre condition")
                print("please request delivery first")
                continue
            print("<< use-case 7 : Refund a package >>")
            print("_request refund service")
            sr = ClientUI.RefundServiceUI()
            sr.sendRefundRequest()
            sr.showResult()
            #time.sleep(3)
           
        else:
            continue
          
    
    
    


#main function
if __name__ == "__main__":
    main()