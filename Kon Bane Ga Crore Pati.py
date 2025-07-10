start="***WELCOME TO KON BANE GA CRORE PATI GAME***\n"
print(start.center(110))
txt=[
    ["Who Is Founder Of Pakistan:\n","Quaid","Iqbal","Liaquat","Benazir","1"],
    ["Which Is Pakistan's Capital:\n","Karachi","Lahore","Islamabad","Peshawar","3"],
    ["Which Is Pakistan's National Sport:\n","Cricket","Football","Baseball","Hockey","4"],
    ["Which Is Largest City Of Pakistan:\n","Karachi","Lahore","Quetta","Peshawar","1"],
    ["When Is Pakistan's Independence Day Celebrated:\n","1945","1947","1949","1948","2"],
    ["When Was Pakistan's Resolution Passed:\n","1942","1947","1940","1948","3"],
    ["Which Is Pakistan's National Animal:\n","Tiger","Markhor","Cow","Lion","2"],
    ["Which Is Pakistan's National Bird:\n","Pigeon","Parrot","Eagle","Shaheen","4"],
    ]
money=0
level=[50000,100000,150000,200000,250000,300000,350000,400000]
choice=int(input("Press 1 To Start The Game OR 0 To Exit The Game: "))
print("\n")
if(choice==1):
    for i in range(0,len(txt)):
        print("Your Question",i+1,"Is Of Rupees:",level[i],)
        text=txt[i]  # We can also use this "print(txt[i][0])" instead of that step.
        print(f"{text[0]}")
        print(f"1) {text[1]}")
        print(f"2) {text[2]}")
        print(f"3) {text[3]}")
        print(f"4) {text[4]}")
        answer=input("\nEnter Your Answer: ")
        if(answer==text[5]):
            print("You have entered correct answer!")
            print("CONGRATULATIONS! YOUR HOME TAKEN MONEY IS :",level[i],"RS TILL NOW.\n")
            money=level[i]
        else:
            print("You have entered wrong answer!")
            break
    if(money==0):
        print("\nSORRY! YOU HAVE LOST THE GAME.\n")
    else:
        print("\nCONGRATULATIONS! YOU HAVE WIN :",money,"Rs From The Game.\n")
elif(choice==0):
    print("THANK YOU FOR PLAYING THE GAME!\n")
else:
    print("WRONG CHOICE ENTERED!\n")