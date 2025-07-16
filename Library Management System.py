text="LIBRARY MANAGEMENT SYSTEM:\n"
print(text.center(115))
class Library:
    def __init__(self):
        self.books=["Holy Quran","Sunnah Of Prophet (PBUH)"]
        self.noofbooks=len(self.books)
    def info(self,book):
        self.books.append(book)
        self.noofbooks=len(self.books)
    def show(self):
        print(f"\nThe Library Has {self.noofbooks} Books Which Are:")
        print("\n")
        i=1
        for x in self.books:
            print(f"BOOK {i}: {x}")
            i+=1
a=Library()
while True:
    print("\nPress 1 To Add Books:")
    print("Press 2 To View Books:")
    print("Press 3 To Exit Library:")
    choice=int(input("Enter Your Choice: "))
    if(choice==1):
        n=int(input("\nHow many books you want to add: "))
        print("\n")
        for y in range(n):
            new_book=input("Enter The Name Of Book: ")
        a.info(new_book)
    elif(choice==2):
        a.show()
    elif(choice==3):
        print("\nTHANK U FOR USING OUR LIBRARY!")
        break
    else:
        print("\nSORRY: WRONG CHOICE ENTERED!")
        break
print("\n")