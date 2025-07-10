text="***SNAKE GUN WATER GAME***\n"
print(text.center(110))
import random 
computer=random.randint(1,3)  # This will import random integer numbers of your given range.
while True:
    print("Press 1 To Start The Game:")
    print("Press 0 To Exit The Game:")
    choice=int(input("Enter Your Choice: "))
    if(choice==1):
        print("\nWELCOME TO THE GAME!")
        print("\nPress 1 For \"SNAKE\":")
        print("Press 2 For \"WATER\":")
        print("Press 3 For \"GUN\":")
        choice1=int(input("Enter Your Choice: "))
        print("\nYour Entered Choice Is:",choice1)
        print("The Computer's Choice Is:",computer)
        if(choice1==1 and computer==3):
            print("\nThe \"SNAKE\" Has Been Killed By \"Gun\".")
            print("SORRY: You Have Lost!\n")
        elif(choice1==2 and computer==1):
            print("\nThe \"Water\" Has Been Drunk By \"Snake\".")
            print("SORRY: You Have Lost!\n")
        elif(choice1==3 and computer==2):
            print("\nThe \"GUN\" Has Been Destroyed By \"WATER\".")
            print("SORRY: You Have Lost!\n")
        elif(choice1==2 and computer==3):
            print("\nThe \"WATER\" Has Destroyed \"GUN\".")
            print("CONGRATULATIONS: You Have Won!\n")
        elif(choice1==3 and computer==1):
            print("\nThe \"GUN\" Has Killed The \"SNAKE\".")
            print("CONGRATULATIONS: You Have Won!\n")
        elif(choice1==1 and computer==2):
            print("\nThe \"SNAKE\" Has Drunk The \"WATER\".")
            print("CONGRATULATIONS: You Have Won!\n")
        elif(choice1==computer):
            print("\nUNFORTUNATELY: The Game Has Drawn!\n")
        else:
            print("\nYour Entered Choice Is Wrong!\n")
    elif(choice==0):
        print("\nTHANK YOU FOR PLAYING THE GAME!\n")
        break
    else:
        print("\nWRONG CHOICE ENTERED!\n")