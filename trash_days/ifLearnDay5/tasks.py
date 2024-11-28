# baho = input("Bahoni kiriting : ")
#
# if baho == "pass":
#     print("Sal Qodli")
# elif baho == 'merit':
#     print("Yomon emas :)")
# elif baho == 'distinetion':
#     print("Bitta story qoyiw joyti )")
# elif baho == 'retake':
#     print("So`ngi pushaymon o`zingga dushman")
# elif baho == 'remodule':
#     print("Bazida chekinish yaxshi ")
# else:
#     print('Invalid input')
#
# Task1
phoneNumber = input("Phone Number : ")
if not phoneNumber.isdigit() and len(phoneNumber) != 9:
    print("Invalid Phone Number")
else:
    if phoneNumber[0] == '9':
        if phoneNumber[1] == '0' or phoneNumber[1] == '1':
            print("Beeline")
        elif phoneNumber[1] == '7':
            print("Mobiuz")
        elif phoneNumber[1] == '9' or phoneNumber[1] == '5':
            print("UzMobile")
        elif phoneNumber[1] == '3' or phoneNumber[1] == '4':
            print("Ucell")
    elif phoneNumber[0] == '8' and phoneNumber[1] == '8':
        print("Mobi uz")
    else:
        print("Bunday Raqam yo`q")
