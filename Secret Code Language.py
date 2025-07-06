text='''"SECRET CODE LANGUAGE"'''
print(text.center(115))
print("\n")
chat=input("Enter Any Text: ")
l=len(chat)
while True:
    print("\nPress 1 For Secret Code Language!")
    print("Press 2 For Decoding Secret Code!")
    print("Press 3 To Exit!")
    choice=(int(input("\nEnter Your Choice: ")))
    if(choice==1):
        if(l<=3):
            print("\nSECRET CODE:",chat[::-1])
        else:
            print("\nSECRET CODE:","abc"+chat[1:][::-1]+chat[0]+"xyz")
    elif(choice==2):
        if(l<=3):
            print("\nDECODED CODE:",chat[0:l])
        else:
            print("\nDECODED CODE:",chat[0:l])
    else:
        print("\nHave A Nice Day!\n")
        break