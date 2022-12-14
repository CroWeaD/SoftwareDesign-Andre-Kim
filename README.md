# README
git clone YOUR_REPO
https://github.com/CroWeaD/SoftwareDesign-Andre-Kim.git

This document describes the test case of the 'Goods Flow Logics System'.
A brief description of each test case and instructions necessary for each test case are described.

##Classes
-------------------------------------------------------------------------------------------------------------------------------------------------------
1. UI.py: UI class.
2. ClientUI.py: UI class for client.
3. CourierInfo.py: UI class for courier.
4. CustomerCompanyInfo.py: UI class for customer company.
5. DataStorage.py: A class that stores data.
6. ManageDelivery.py: A class to manage delivery services.
7. ManageProfile.py: A Class to manage profile modifications.
8. ManageRefundService.py: A class to manage refund services.
9. ManageSendService.py: A class to manage send services.
10. ManageSignIn.py: A class to manage sign in.
11. ManageSignUp.py: A class to manage sign up.
12. ManageTracking.py: A class to manage tracking services.
13. main.py: A class that can simulate all test cases with UI.
14. TestCase.py : A class that can each test case run.

##Test Cases
-------------------------------------------------------------------------------------------------------------------------------------------------------
TC1. Sign up

It is a test case for sign up.

Command line: python3 -m unittest TestCase.ProfileTests.test_case1

Prerequisites

Account information has the following order:
[user's ID, user's password, user's phone number, user's address].

Test Steps

1. Enter user's ID (input: Arooba)

2. Enter user's password (input: 1234)

3. Enter user's phone number (input: 010-1234-5678)

4. Enter user's address (input: Daegu)

Result

<< test-case 1 : Sign up >>
_request sign-up
ID: Arooba
passwd: 1234
phonenum (ex - 010-1234-5678): 010-1234-5678
address: Daegu
_signUp()
_validateSignUp()
_insert() (<actor>Data_Storage —> Data Storage)
['root', '1234', '010-1234-5678', 'Address']
['Arooba', '1234', '010-1234-5678', 'Daegu']
_result (True or False)
_showResult()
—————————————
True
—————————————

-------------------------------------------------------------------------------------------------------------------------------------------------------
TC2. Sign in

It is a test case for sign in.

Command line: python3 -m unittest TestCase.ProfileTests.test_case2

Prerequisites

There are an root's account that 
["root", "1234", "010-1234-5678", "Address"] 
in data storage already.

Test Steps

1. Enter user's ID (input: root)

2. Enter user's password (input: 1234)

Result
  
<< test-case 2 : sign in >>
_request sign_in
ID<The default id is 'root'>: root
passwd<the default password is '1234'>: 1234
_signIn()
_validateSignIn()
_select() (<actor>Data_Storage —> Data Storage)
_return
_result (True or False)
_showResult()
—————————————
True
—————————————

-------------------------------------------------------------------------------------------------------------------------------------------------------
TC3. Update profile

It is a test case that modifies the profile.

Command line: python3 -m unittest TestCase.ClientTests.test_case3

Prerequisites

There are an root's account that
["root", "1234", "010-1234-5678", "Address"]
 in data storage already.

Already sign in root's account.

If the input is NULL, that information is not modified.

Test steps

1. Enter user's new password (input: 0000)

2. Enter user's new phone number (input: NULL)

3. Enter user's new address (input: NULL)

Result

<< test-case 3 : Update a profile >>
_update a profile
passwd: 0000
phonenum (ex - 010-1234-5678): 
address: 
_sendProfile()
_updateProfile()
_update() (<actor>Data_Storage —————————————> Data Storage)
_return
_result
_showResult()
—————————————
Changed ['root', '0000', '010-1234-5678', 'Address']
—————————————

-------------------------------------------------------------------------------------------------------------------------------------------------------
TC4. Delivery service

It is a test case in which the customer company requests delivery to the system.

Command line: python3 -m unittest TestCase.CCTest.test_case4

Prerequisites

Order information has the following order:
[order number, package name, cost, client name, receiver, arrive point, phone number, message, payment type, sender, start point].
Courier information has the follwing order:
[courier name, tracking number, contract code].

There are an order information that 
["20210325OXjG8", "I-pad_air_5", "750,000", "root", "Andre_Kim", "knu_IT-5_341", "010-1234-5678", "please_fast", "card", "APPLE", "California"]
 in data storage already.

There are a courier information that
["11ST_1234", "EG033025977JA", "3-17"]
 in data storage already.

Test steps

There are not neccessery input data.

Result
  
<< test-case 4 : request delivery >>
_Reqeust a delivery service
_sendinformation()
_addInformation() (order information)
_insert() (<actor>Data_Storage --> Data Storage)
_transferOrderInformation()
order number    : 20210325OXjG8
package name    : I-pad_air_5
cost            : 750,000
client name     : root
receiver        : Andre_Kim
arrive point    : knu_IT-5_341
phone number    : 010-1234-5678
message         : please_fast
payment Type    : card
sender          : APPLE
start point     : California
_sendOrderInformation() (CourierInfo --> courier)
_send a tracking number and contract code(courier --> CorierInfo)
ex)
corier name     : 11ST_1234
tracking number : EG033025977JA
contract code   : 3-17
_sendCourirerInformation()
_addInformation() (courier information)
_insert() (<actor>Data_Storage —> Data Storage)
_transferCourierInformation()
Data_Storage
orderInfo       : ['20210325OXjG8', 'I-pad_air_5', '750,000', 'root', 'Andre_Kim', 'knu_IT-5_341', '010-1234-5678', 'please_fast', 'card', 'APPLE', 'California']
courierInfo     : ['11ST_1234', 'EG033025977JA', '3-17']
_showResult()
—————————————
request success…
['11ST_1234', 'EG033025977JA', '3-17']


-------------------------------------------------------------------------------------------------------------------------------------------------------
TC5. Tracking service

It is a test case in which the Client uses the delivery tracking service.

Command line: python3 -m unittest TestCase.ClientTests.test_case5

Prerequisites

There are an order information that 
["20210325OXjG8", "I-pad_air_5", "750,000", "root", "Andre_Kim", "knu_IT-5_341", "010-1234-5678", "please_fast", "card", "APPLE", "California"]
 in data storage already.

There are a courier information that
['11ST_1234', 'EG033025977JA', '3-17']
 in data storage already.

There are a tracking information that be inserted in order
['California', 'hub_1', 'hub_2', 'hub_3', 'knu_IT-5_341']
in data storage already.

Already sign in root's account.

Test steps

There are not neccessery input data.

Result
  
_request sign_in
_signIn()
_validateSignIn()
_select() (<actor>Data_Storage --> Data Storage)
_return
_result (True or False)
_showResult()
True
<< test-case 5 : track a package >>
_Reqeust a delivery service
_sendinformation()
_addInformation() (order information)
_insert() (<actor>Data_Storage --> Data Storage)
_transferOrderInformation()
order number    : 20210325OXjG8
package name    : I-pad_air_5
cost            : 750,000
client name     : root
receiver        : Andre_Kim
arrive point    : knu_IT-5_341
phone number    : 010-1234-5678
message         : please_fast
payment Type    : card
sender          : APPLE
start point     : California
_sendOrderInformation() (CourierInfo --> courier)
_send a tracking number and contract code(courier --> CorierInfo)
ex)
corier name     : 11ST_1234
tracking number : EG033025977JA
contract code   : 3-17
_sendCourirerInformation()
_addInformation() (courier information)
_insert() (<actor>Data_Storage --> Data Storage)
_transferCourierInformation()
Data_Storage
orderInfo       : ['20210325OXjG8', 'I-pad_air_5', '750,000', 'root', 'Andre_Kim', 'knu_IT-5_341', '010-1234-5678', 'please_fast', 'card', 'APPLE', 'California']
courierInfo     : ['11ST_1234', 'EG033025977JA', '3-17']
_showResult()
request success...
['11ST_1234', 'EG033025977JA', '3-17']
_request a tracking information
_sendTrackingRequest()
_requestTrackingService()
_requestTracking()(CourierInfo --> courier)
_tracking information(corier —> CorierInfo)
_sendTrackingInformation()
California
_sendTrackingInformation()
hub_1
_sendTrackingInformation()
hub_2
_sendTrackingInformation()
hub_3
_sendTrackingInformation()
knu_IT-5_341
_addInforamtion() (tracking information)
_insert() (<actor>Data_Storage —> Data Storage)
_transferTrackingInformation()
Data_Storage
trackingInfo    : ['California', 'hub_1', 'hub_2', 'hub_3', 'knu_IT-5_341']
_showResult()
['California', 'hub_1', 'hub_2', 'hub_3', 'knu_IT-5_341']

-------------------------------------------------------------------------------------------------------------------------------------------------------
TC6. Sending service

It is a test case in which the client uses the system's send service.

Command line: python3 -m unittest TestCase.ClientTests.test_case6

Prerequisites

Send information has the following order.
[order number, package name, cost, send, phone number, start point, receiver, receiver's phone number, arrive point, package type, payment type]

There are a send information that 
["20210325OYDG3", "I-pad_pro", "100,000", "Andre_Lee", "010-1212-1212", "2_chung_dam", "Andre Park", "010-3434-3434", "knu_IT-5_341", "normal", "Cash on delivery"] 
in data storage already.

There are a courier information that
['CU_5935', 'HG032632975JB', '5-34']
 in data storage already.

There are a tracking information that be inserted in order
['2_chung_dam', 'hub_1', 'hub_2', 'hub_3', 'knu_IT-5_341']
in data storage already.

Already sign in root's account.

Test steps

There are not neccessery input data.

Result
  
_request sign_in
_signIn()
_validateSignIn()
_select() (<actor>Data_Storage --> Data Storage)
_return
_result (True or False)
_showResult()
True
<< test-case 6 : send a package >>
_request send a package
_sendSendingRequest()
_addInformation() (sending information)
_insert() (<actor>Data_Storage --> Data Storage)
_requestSendingService()
order number    : 20210325OYDG3
package name    : I-pad_pro
cost            : 100,000
sender          : Andre_Lee
phone number    : 010-1212-1212
start point     : 2_chung_dam
receiver        : Andre Park
phone number    : 010-3434-3434
arrive point    : knu_IT-5_341
package type    : normal
payment type    : Cash on delivery
_requestSending (CourierInfo --> courier)
_send a tracking number and contract code(courier --> CorierInfo)
ex)
corier name     : CU_5935
tracking number : HG032632975JB
contract code   : 5-34
_sendCourirerInformation()
['CU_5935', 'HG032632975JB', '5-34']
_addInformation() (courier information)
_insert() (<actor>Data_Storage --> Data Storage)
_requestTrackingInfo()
_requestTracking()(CourierInfo --> courier)
_tracking information(corier --> CorierInfo)
_sendTrackingInformation()
2_chung_dam
_sendTrackingInformation()
hub_1
_sendTrackingInformation()
hub_2
_sendTrackingInformation()
hub_3
_sendTrackingInformation()
knu_IT-5_341
_addInformation() (tracking information)
_insert() (<actor>Data_Storage --> Data Storage)
_transferTrackingInformation()
Data_Storage
sendingInfo     : ['20210325OYDG3', 'I-pad_pro', '100,000', 'Andre_Lee', '010-1212-1212', '2_chung_dam', 'Andre Park', '010-3434-3434', 'knu_IT-5_341', 'normal', 'Cash on delivery']
courierInfo     : ['CU_5935', 'HG032632975JB', '5-34']
trackingInfo    : ['2_chung_dam', 'hub_1', 'hub_2', 'hub_3', 'knu_IT-5_341']
_showResult()
—————————————
['2_chung_dam', 'hub_1', 'hub_2', 'hub_3', 'knu_IT-5_341']

-------------------------------------------------------------------------------------------------------------------------------------------------------
TC7. Refund service

It is a test case in which the client uses the system's refund service.

Command line: python3 -m unittest TestCase.ClientTests.test_case7

Prerequisites

The refund information is stored in the data store in the same order as the order information.

There are an order information that
["20210325OXjG8", "I-pad_air_5", "750,000", "root", "Andre_Kim", 
"knu_IT-5_341", "010-1234-5678", "please_fast", "card", "APPLE", "California"]
in data storage already.

There are a courier information that
['11ST_1234', 'EG033025977JA', '3-17']
 in data storage already.

There are a tracking information that be inserted in order
['knu_IT-5_341', 'hub_3', 'hub_2', 'hub_1', 'California']
in data storage already.

Already sign in root's account.

Test steps

There are not neccessery input data.

Result
  
_request sign_in
_signIn()
_validateSignIn()
_select() (<actor>Data_Storage --> Data Storage)
_return
_result (True or False)
_showResult()
True
<< test-case 7 : Refund a package >>
_Reqeust a delivery service
_sendinformation()
_addInformation() (order information)
_insert() (<actor>Data_Storage --> Data Storage)
_transferOrderInformation()
order number    : 20210325OXjG8
package name    : I-pad_air_5
cost            : 750,000
client name     : root
receiver        : Andre_Kim
arrive point    : knu_IT-5_341
phone number    : 010-1234-5678
message         : please_fast
payment Type    : card
sender          : APPLE
start point     : California
_sendOrderInformation() (CourierInfo --> courier)
_send a tracking number and contract code(courier --> CorierInfo)
ex)
corier name     : 11ST_1234
tracking number : EG033025977JA
contract code   : 3-17
_sendCourirerInformation()
_addInformation() (courier information)
_insert() (<actor>Data_Storage --> Data Storage)
_transferCourierInformation()
Data_Storage
orderInfo       : ['20210325OXjG8', 'I-pad_air_5', '750,000', 'root', 'Andre_Kim', 'knu_IT-5_341', '010-1234-5678', 'please_fast', 'card', 'APPLE', 'California']
courierInfo     : ['11ST_1234', 'EG033025977JA', '3-17']
_showResult()
request success...
['11ST_1234', 'EG033025977JA', '3-17']
_request refund service
_sendRefundRequest()
_sendRefundInformation()
_showRefundInformation()
client request refund
_requestRefundService()
_requestRetrieve() (CorierInfo --> corier)
_send a tracking number and contract code(courier --> CorierInfo)
ex)
corier name     : CU_5935
tracking number : HG032632975JB
contract code   : 5-34
_sendCourirerInformation()
_addInformation() (courier information)
_insert() (<actor>Data_Storage --> Data Storage)
_requestTrackingInfo()
_requestTracking()(CourierInfo --> courier)
_tracking information(corier --> CorierInfo)
_sendTrackingInformation()
knu_IT-5_341
_sendTrackingInformation()
hub_3
_sendTrackingInformation()
hub_2
_sendTrackingInformation()
hub_1
_sendTrackingInformation()
California
_addInformation() (tracking information)
_insert() (<actor>Data_Storage --> Data Storage)
_transferTrackingInformation()
Data_Storage
courierInfo     : ['11ST_1234', 'EG033025977JA', '3-17']
TrackingInfo    : ['knu_IT-5_341', 'hub_3', 'hub_2', 'hub_1', 'California']
_showResult()
['knu_IT-5_341', 'hub_3', 'hub_2', 'hub_1', 'California']
