print("----------------------------------------")
print("           COVI MOBILE SHOPE            ")
print("----------------------------------------")

def menu():

    print("\nWELCOME TO COVI MOBILE SHOPE\n")
    print("\n1. MOBILE INFOTMATION\n2. MOBILE BUYING\n")

    user = int(input("Enter your choice:"))
    
    if user ==1:
        print("-----------------------------------")
        print("        MOBILE INFOTMATION         ")
        print("-----------------------------------")
        print("1) iphone\n")

        user_city = int(input("Choice your wanted place:"))

        if user_city == 1:
            print("\niphone information\n")
            print("1) iphone12\n2) iphone13\n3) iphone14")

            iphone_version = int(input("\n Choice your want iphone version:"))

            if iphone_version == 1:
                print("\nWelcome to iphone12 version")
                print("\nWe have only iphone12 pro")
                print("\nThis version relace version in 2020")
                print("\nThis Mobile version price is Rs.89,000")
            
            elif iphone_version == 2:
                print("\nWelcome to iphone13 version")
                print("\nWe have only iphone13 pro")
                print("\nThis version relace version in 2021")
                print("\nThis Mobile version price is Rs.1,15,000")
            
            elif iphone_version == 2:
                print("\nWelcome to iphone14 version")
                print("\nWe have only iphone14 pro")
                print("\nThis version relace version in 2022")
                print("\nThis Mobile version price is Rs.1,35,000")

            else:
                print("** Please give valuable information **")

            ask = input("Do you want to continue(YES/No):").lower()

            if ask == "yes":
                user = int(input("Enter your choice:"))
                main_function()
            else:
                print("Thank to come....Have nice journey")
            
    
    elif user ==2:
        print("-----------------------------------")
        print("          BOOKING TICKETS          ")
        print("-----------------------------------")
        print("1) iphone12\n2) iphone13\n3) iphone14")

        ticktes=["iphone12","iphone13","iphone14"]

        iphone12_amount=1000
        iphone13_amount=500
        iphone14_amount=800

        your_ticktes=input("\nEnter your Destination:").upper()

        if your_ticktes in ticktes:
            print(f"\nyes!...{your_ticktes} ticktes is available")
            how_many=int(input(f"\nhow many {your_ticktes} ticktes you want:"))
            if your_ticktes=="COIMBATORE":
                total=coimbatore_amount*how_many
                if total>=5000:
                    final_total=total-500
                    print(f"\nyour total bill is {total}\n offer 500 so,your final total is {final_total}")
                else:
                    print(f"\nyou orderded {how_many} tickets so,your total bill is {total}")

            elif your_ticktes=="MADURAI":
                total=madurai_amount*how_many
                if total>=3000:
                    final_total=total-300
                    print(f"\nyour total bill is {total}\n offer 300 so,your final total is {final_total}")
                else:
                    print(f"\nyou orderded {how_many} tickets so,your total bill is {total}")

            elif your_ticktes=="SALEM":
                total=salem_amount*how_many
                if total>=4000:
                    final_total=total-400
                    print(f"\nyour total bill is {total}\n offer 200 so,your final total is {final_total}")
                else:
                    print(f"\nyou orderded {how_many} tickets so,your total bill is {total}")

        else:
            print("Choose your right choice")
        
        ask = input("\nDo you want to continue(YES/No):").lower()

        if ask == "yes":
            main_function()
        else:
            print("Thank to come....Have nice journey")

def feedback():    

    print("-----------------------------------")
    print("             Feedback              ")
    print("-----------------------------------")
    
    user_feedback = input("\nEnter your feedback:")
    feedback = []
    feedback.append(feedback)
    if user_feedback:
        print(f"\n Your Feedback is successfully Added.\n")
        print("Comeing again.")
    else:
        print("Please leave your feedback")

    ask = input("\nDo you want to continue(YES/No):").lower()

    if ask == "yes":
        main_function()
    else:
        print("Thank to come....Have nice journey")
        
def login():

    print("\n WELCOME TO MANI BUS TRAVELS\n")
    print("1. SIGN UP\n2. SIGN IN")

    user = int(input("\n Enter your choice:"))

    if user == 1:
        print("\n WELCOME TO SIGNUP PAGE\n")
        print("Please Enter your singup details\n")

        user_name = input("Enter your Name:")
        user_phone_number = int(input("\n Enter your phone number: "))
        user_mail = input("\n Enter your Valuale Mail ID:")
        user_password = int(input("\n Enter your password:"))

        print(f"{user_name}, your are successfully singup \n")
        print(f"CHECK OUT YOUR INFORMATION,\nYour Name is = {user_name},\n Your phone number= {user_phone_number},\n Your mailID = {user_mail}")

        # user_name = []
        # user_phone_number = []
        # user_mail = []
        # user_password = []

        # user_name.append(user_name)
        # user_phone_number.append(user_phone_number)
        # user_mail.append(user_mail)
        # user_password.append(user_password)

    elif user == 2:
        print("\n WELCOME TO SIGNIN PAGE\n")
        print("Please Enter your singin details\n")

        user_name = input("Enter your username/mailid:").upper()
        user_password = input("\nEnter your password:")

        print(f"\n{user_name},You are successfully signin this page.")
        
    ask = input("\nDo you want to continue(YES/No):").lower()

    if ask == "yes":
        main_function()
    else:
        print("Thank to come....Have nice journey")

def main_function():

    print('''1. MENU\n2. FEEDBACK\n3. LOGIN\n''')
    user = int(input("Enter your choice:"))
    if user ==1:
        menu()
    elif user ==2:
        feedback()
    elif user == 3:
        login()
    else:
        print("\n ******* Please choose your right choice *******")

main_function()