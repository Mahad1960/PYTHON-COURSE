text='''"QUIZ MANAGEMENT SYSTEM:"'''
print(text.center(120))
count=0
g='''\n1) How Many Provinces In Pakistan Are?\n\na) 4\nb) 6\nc) 5\nd) 3\n'''
print(g)
choice1=input("\nEnter Your Choice: ")
check1=choice1.lower()
if(check1=='c'):
  print("You Have Entered A Correct Answer!")
  count+=1
else:
  print("You Have Entered A Wrong Answer!")
a='''\n2) Which Is Pakistan's Biggest City?\n\na) Karachi\nb) Islamabad\nc) Larkana\nd) Lahore\n'''
print(a)
choice2=input("\nEnter Your Choice: ")
check2=choice2.lower()
if(check2=='a'):
  print("You Have Entered A Correct Answer!")
  count+=1
else:
  print("You Have Entered A Wrong Answer!")                   
print("\n")
text='''"RESULT:"'''
print(text.center(120))
if(count==2):
  print("CONGRATULATIONS: You Have A Great IQ!")
elif(count==1):
  print("CONGRATULATIONS: But You Can Improve!")
else:
  print("SORRY: Better Luck Next Time!")