ticktes=["coimbatore","madurai","salem"]

coimbatore_amount=1000
madurai_amount=500
salem_amount=800
your_ticktes=input("enter your tickts:")

if your_ticktes in ticktes:
    print(f"yes!...{your_ticktes} ticktes is available")
    how_many=int(input(f"how many {your_ticktes} you want:"))
    if your_ticktes=="coimbatore":
        total=coimbatore_amount*how_many
        if total>=5000:
            final_total=total-500
            print(f"your total bill is {total}\n offer 500 so,your final total is {final_total}")
        else:
            print(f"you orderded {how_many} tickets so,your total bill is {total}")

    elif your_ticktes=="madurai":
        total=madurai_amount*how_many
        if total>=3000:
            final_total=total-300
            print(f"your total bill is {total}\n offer 300 so,your final total is {final_total}")
        else:
            print(f"you orderded {how_many} tickets so,your total bill is {total}")

    elif your_ticktes=="salem":
        total=salem_amount*how_many
        if total>=4000:
            final_total=total-400
            print(f"your total bill is {total}\n offer 200 so,your final total is {final_total}")
        else:
            print(f"you orderded {how_many} tickets so,your total bill is {total}")

    else:
        print("Choose your right choice")

else:
        print("Choose your right choice")