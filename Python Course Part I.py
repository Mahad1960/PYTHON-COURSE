print("\nCOMBINATION OF STRINGS AND NUMBERS IN ONE PRINT STATEMENT: Hello World!","WOW",10.5,5)
print("DIGIT : ",56)
print("CALCULATION : ",10*15)
# Modules are basically files that contain (functions,variables,classes etc) and are used to reuse code.
import math # This is built-in module.
print("SQUARE ROOT OF 25 IS:",math.sqrt(25))
import pandas # This is user-defined module which we create using PIP.
print("\nMy Name Is \"Mahad Shahnawaz\".")
print("I Study In FAST ", 2,sep="~",end=" University.\n")
a=5
print("\nNUMBER:",a)
print("The Type Of a is: ",type(a))
b=complex(8,4)
print("COMPLEX NUMBER:",b)
print("The Type Of b is: ",type(b))
# list and tuple are collection of datatypes.
# list is mutable while tuple is immutable.
# dict means key value pairs.It is basically mapped data.
# In PYTHON every thing is object.
print("DIVISION WITH DECIMAL:",15/6)
print("DIVISION WITHOUT DECIMAL:",15//6)
print("MODULUS:",15%6)
print("EXPONENT:",5**2)
x="2"
y="4"
print("SUM OF NUMBERS IN STRING IS:",int(x)+int(y))
# While taking input, everything is taken as string by PYTHON.
z=input("\nEnter Your Age: ")
print("Your Age Is:",z)
c=input("\nEnter Your First Name: ")
d=input("Enter Your Last Name: ")
print("Your Full Name Is:",c+d)
print("\nHELLO, ",c,d)
e=input("\nEnter 1st Number: ")
f=input("Enter 2nd Number: ")
print("Sum Of Two Numbers Is:",int(e)+int(f))
print("\n")
# You can also write a string in PYTHON like that:
str='''HELLO!
My name is "Mahad Shahnawaz" and I study in FAST NUCES.'''
print(str)
print("\n")
# Printing the string using FOR loop.
name="Mahad Shahnawaz"
# You can use any alphabet or word on "i" place.
for i in name:
  print(i) 
print("\n")
# Using for loop in lists.
color=["RED","GREEN","BLUE"]
for x in color:
  print(x)
  for y in x:
    print(y)
print("\n")
length=len(name)
print("Your name has",length,"words including spaces.")
print("Method Of Complete Name Writing:",name[:])
print("1st Method Of Name:",name[0:5]) # Including 0 but not 5
print("2nd Method Of Name:",name[:5])
# These two following methods are same.
print("3rd Method Of Name:",name[0:-3])
print("4th Method Of Name:",name[:len(name)-3])
# In 5th method, PYTHON will use len on both sides.So, 1st number must be greater than 2nd nummber.Ignore sign
print("5th Method Of Name:",name[-4:-2]) 
# Strings are immutable.They work on existing string but return a new string.
print("\n")
print("Name In Uppercase:",name.upper())
print("Name In Lowercase:",name.lower())
print("\n")
# rstrip doesn't remove leading characters because it removes trailing characters.
non="Mahad Shah!!!!"
print(non.rstrip("!"))
# While replacing must take care of uppercase or lowercase. 
print(non.replace("Mahad","Simra"))
# For split your string must contain spaces but it is not compulsory.
print(non.split(" "))
text="my Name is Mahad Shahnawaz."
# Capitalize only makes 1st letter capital and makes other letters in lowercase in string.
print("\nCAPITALIZE:",text.capitalize())
print(text.center(80))
print("\nYour text has",text.count("a"),"times same character.")
# You must have to check upper or lower case for endswith or startswith.
print("ENDSWITH:",text.endswith("."))
print("ENDSWITH:",text.endswith("s ",5,11))
print("STARTSWITH:",text.startswith("m"))
# Find will tell the occurence/index of 1st letter in string.
# If Find not finds the occurence/index it will return -1.
print("FIND:",text.find("ah"))
# Index works same as Find but the difference is that it displays an error if occurence is not found.
# isalnum gives true if string contains only A-Z,a-z,0-9 otherwise it gives false.
print("IS ALNUM:",text.isalnum())
# isalpha gives true if A-Z or a-z is present otherwise false.
print("IS APLHA:",text.isalpha())
# islower gives true if string is in lowercase otherwise false.
# isupper gives true if string is in uppercase otherwise false.
print("IS LOWER:",text.islower())
print("IS UPPER:",text.isupper())
# isprintable gives if string is printable or not.It gives false if newline character is present etc.
print("IS PRINTABLE:",text.isprintable())
# isspace gives true if string contain spaces otherwise false.
print("IS SPACE:",text.isspace())
# istitle gives true if 1st letter of each word is capital.
print("IS TITLE:",text.istitle())
# swapcase converts upper to lower or upper to lower case.
print("SWAP CASE:",text.swapcase())
# title capitalize each word of string.
print("TITLE:",text.title())
print("\n")
j=20
# These following conditional operators gives answers as true/false.
print(j<=18)
print(j>=18)
print(j==18)
print(j!=18)
num=int(input("\nEnter Any Number: "))
# Match statement works as switch statement.
match num:
# If you don't give space before case, it will give error.
# If the input number is 5 it will display output on 1st occurence and will not go in default statement.
# There is no use of break in cases.
  case 0:
    print("Number is zero.")
  case 5:
    print("Number is five.")
# The following is used for default purpose.You can also use if statements with default statements.
  case _ if num==10:
    print("The number I suppose is to be 10. Maybe I am wrong.")
  case _:  # If above default statement doesn't work then this statement will work.
    print("Your entered number is",num)
# Use of RANGE.
print("\n")
for a in range(5): # It will not include 5 and starts from 0.
  print(a)
print("\n")
for b in range(8): # It will include 8 and starts from 1 because you have used b+1.
  print(b+1)
print("\n")
for c in range(1,10): # It will include 1 but not 10 and displays number between them.
  print(c)
print("\n")
for d in range(1,15,3): # It will work as above but give difference of 3 between each number.
  print(d)
print("\n")
for e in range(5,0,-1): # This will reverse counting but it will work only when 1st>2nd number.
  print(e)
print("\n")
# Using While Loop with Else Statement.
i=int(input("Enter Any Number Except 4 and so on: "))
while(i<4):
  i=int(input("Enter Any Number Except 4 and so on: "))
else:
  print("Your while loop work is done and now you are inside else loop.")
print("\n")
# PYTHON doesn't have do-while loop but we can create it using while true loop and break statement.
for i in range(1,11):
  print("5 x",i,"=",5*i)
# Use of Break.Break skips that loop in which it is present.
  if(i==5):
    break
# Use of Continue.Continue just skips the current iteration.
print("\n")
# Functions are : Built-in and User-defined.
# User-defined Functions use def keyword.
# Built-in Functions are already designed like len(),range(),list(),max() etc.
def average(a,b):
  avg=(a+b)/2
  print("Average Of",a,"and",b,"Is:",avg)
def check(a,b):
  if(a>b):
    print(a,"Is Greater than",b)
  elif(b>a):
    print(b,"Is Greater than",a)
  else:
    print(a,b,"are equal.")
# If i want to create a function and u decided to write its body later then use "pass" keyword, otherwise it will give error.
def sum(c,d):
  pass
c=int(input("Enter 1st Number: ")) # If you don't use int here it will give an error.
d=int(input("Enter 2nd Number: "))
average(c,d)
check(c,d)
print("\n")
# Function Arguments:
def multiply(a=4,b=3):
  print("The Multiplication of",a,"and",b,"is:",a*b)
multiply()          # OUTPUT=12
# multipy(5,3)      # a=5,b=3 work and a=4,b=3 will not work.
# multiply(6)       # a=6,b=3 will work and a=4 will be ignored.
# multiply(b=2)     # a=4,b=2 will work and b=3 will not work.
# multiply(b=7,a=8) # In this case,a=4,b=3 will not work.
# If you are passing 3 arguments then the last one must be defined in function arguments.
# EXAMPLE:
# def example(a,b,c=3)
# example(3,4)
# Other Method Of Function:
# Now, num will be delt as tuple.
# Print Method:
def sub(*num):
  answer=0
  for i in num:
    answer=answer-i
  print("SUBTRACTION USING PRINT:",answer)
sub(1,4,6,8,-10)
# Return Method:
def sub(*num):
  answer=0
  for i in num:
    answer=answer-i
  return answer
z=sub(1,4,6,8,-10)
print("SUBTRACTION USING RETURN:",z)
# If you use more than one "return" then only 1st one will execute and the 2nd one will not be executed.
print("\n")
# Use Of List:
x=["Mahad",3,True,5.2,"Mango"]
print("All Elements Of List:",x)      # It will print all elements of list.
print("All Elements Of List:",x[:])   # It will print all elements of list.
print("Some Indexes:",x[::2]) # It will print all elements by jumping one index.
print("0th Index:",x[0])  # By using index you can print any element of list.
print("2nd Index:",x[-3]) # In this case, print will work as [len(x)-3]="2" and this index will be printed.
# Checking elements in list.
if 5.2 in x: 
  print("Found in List!")
else:
  print("Not Found in List!")
# This can also be used for checking simple strings.
if "Ma" in "Mahad": # Must take care of upper and lower case.
  print("Found in String!")
else:
  print("Not Found in String!")
print("\n")
# List Comprehension:
# Don't use space in start of print in the following.
lst=[i*i for i in range(6)] # You can perform anything in place of "i*i" like (i+i, i, i/i).
print("LIST COMPREHENSION:",lst)
lst=[i for i in range(10) if(i%2==0)] #Using IF Condition.
print("LIST COMPREHENSION USING CONDITION:",lst)
lst=[i if(i%2==0) else "Not Required:" for i in range(10)] #Using IF And ELSE Condition.
print("LIST COMPREHENSION USING  2 CONDITIONS:",lst)
print("\n")
# Appending Elements In List.
l=[1,9,7,5,7]
print("Actual List:",l)
l.pop(3)
print("List After Using POP:",l)
l.append(int(input("Enter Any Number To Append: "))) # If i don't use "int" here, it will display output in inverted single commas. 
print("After Appending:",l)
# Use Of Insert:
l.insert(0,17)
print("Inserted List:",l) # It insert an element on your given index and shifts rest by +1.
# 1st Method Of Extending List:
m=[13,15,17]
print("New List:",m)
l.extend(m)
print("1st Method Of Extended List:",l)
# 2nd Method Of Extending List:
n=l+m
print("2nd Method Of Extended List:",n)
# Sorting In Ascending:
l.sort()
print("Sorted List In Ascending:",l)
# Sorting In Descending:
l.sort(reverse=True)
print("Sorted List In Descending:",l)
# Reversing The List:
l.reverse()
print("Reversed List:",l)
# Printing Index Of List.
print("7 Number is on",l.index(7),"index of List.") # It finds and display the index of your entered number.If there are two same numbers in list it will give output on 1st occurence.
# Counts the number in List.
print("7 number is found",l.count(7),"times in List.")
# You can change elements in list by following methods:
# How COPY works:
# CONCEPT:1
# m=l      # It will copy contents of "l" in "m".
# m[0]=0
# print(l) # It will change contents of "l" as well because of above step.
# CONCEPT:2
m=l.copy()  # It will copy contents of "l" in "m" but will not effect "l".
m[0]=0
print("COPIED LIST IN NEW VARIABLE WITH CHANGES:",m)    # It will not change contents of "l".
print("\n")
# Use Of Tuple:
tup=(7,2,"Mahad",True,4.2,"Shah",3,5.0,7,3) 
# tup=(1)                       # This will indicate "int".
# If you want it as tuple write tup=(1,) ,then tuple will be created.
# tup[0]=5                      # Tuple can't be changed, this will give error.
print("All Elements Of Tuple:",tup)      # It will print all elements of list.
print("All Elements Of Tuple:",tup[:])   # It will print all elements of list.
print("Some Indexes:",tup[::2]) # It will print all elements by jumping one index.
print("0th Index:",tup[0])      # By using index you can print any element of list.
print("2nd Index:",tup[-3])     # In this case, print will work as [len(x)-3]="2" and this index will be printed.
print("The length Of Your Tuple Is:",len(tup))
r=tup.count(1)
print("7 is found",r,"times in tuple.")
print("7 Number is on",tup.index(7),"index of Tuple.") # It finds and display the index of your entered number.If there are two same numbers in tuple it will give output on 1st occurence.
print("3 number b/w 2nd and 8th index is found on",tup.index(3,2,8),"index.") # The number you want to check should be written first, otherwise it displays an error.
if 4.2 in tup: 
  print("Found in Tuple!")
else:
  print("Not Found in Tuple!")
print("\n")
# You can't change size of Tuple.
tup2=tup  # You can also use like this: tup2=tup[1:3]
print("COPIED TUPLE IN NEW VARIABLE:",tup2)
# Concatenating Tuple:
j=(1,"Spain",4.0,"India",7)
k=(True,"Pakistan")
l=j+k # Remember this that "l" is a new tuple which is combination of two tuples.
print("CONCATENATED TUPLE:",l)
# How To Change Tuple:
countries=("Russia","England","Italy","Germany","India")
print("Actual Tuple:",countries)
temp=list(countries)
temp.append("Pakistan")
temp.pop(4)
temp[0]="Spain"
countries=tuple(temp)
print("TUPLE WITH CHANGES:",countries)
u=(0,5,7,9,1,3)
temp=list(u)
temp=sorted(temp)
u=tuple(temp)
print("SORTED TUPLE",u)
print("\n")
# Use Of Format.
letter="My Name Is {} and I Live In {}." # If you use "1" in 1st bracket and "0" in 2nd bracket then country will be printed first and then name will be printed. 
name="Mahad Shahnawaz"
country="Pakistan"
salary=50000.100000
uni="FAST NUCES"
sem="2nd Semester"
print("STRING FORMAT:",letter.format(name,country))
# If you want to print same letter with this "{name} and {country}", then use {{}}.
# Use Of fstring.
print(f"STRING F: It Is My {sem} now and I Study In {uni}.")
print(f"STRING F: My Salary Is {salary:.2f} Dollars per month.")
print("\n")
# Use Of Docstrings.
# Docstring should be written before function body, otherwise it will not work.
def square(n):
  '''Squaring A Number In A Function'''  # This Line Will Be Printed Using "DOC".
  print("The Square Of 5 is:",n**2)      # This Syntax Will Do Squaring.
square(5)
print("DOC STRING:",square.__doc__)
print("\n")
# import this --> this will give ZEN OF PYTHON (A Poem).
# RECURSION:
def factorial(n):
  if(n==1 or n==0):
    return 1
  else:
    return n*factorial(n-1)
value=int(input("Enter Any Number: "))
result=factorial(value)
print("Factorial Of",value,"Is:",result)
def fibonacci(n):
  if(n==1):
    return 1
  elif(n==0):
    return 0
  else:
    return fibonacci(n-1) + fibonacci(n-2)
val=int(input("\nEnter The Number Of Outcomes You Want For Fibonacci Series: "))
series=[]
for i in range(val):
    series.append(fibonacci(i))
print("FIBONACCI SERIES:", series)
print("\n")
# Use Of Sets:
# Sets doesn't give output in order.
# Use these:"{}" brackets for sets/dict.
s={2,4,6,8,2}
t={"Naeem",True,8.0,"Mahad","Naeem",6}
print("SET 1:",s) # Sets basically prints repeated value once.
print("SET 2:",t)
# Adding Element In Set:
s.add("10")
print("SET 1 After Addition:",s)
# Removing Element From Set:
# You can also use "discard" here but the difference between discard and remove is:
# If element not found "remove" shows error and stop the program while "discard" doesn't give error and continues executing the program.
s.remove("10")  
print("SET 1 After Discarding 10:",s)
s.pop()  # POP randomly deletes an item from set.
print("SET 1 After Using POP:",s) 
# Checking Elements In SET:
if "Mahad" in t:
  print("Mahad Is Present In Set 2.")
else:
  print("Mahad Is Not Present In Set 2.")
# del s                   # "DEL" is used to delete entire set.
# print("DELETE SET:",s)  # It will give error.
t.clear() # It is used to clear all elements in entire set which means that set will become empty
print("CLEARING SET 2:",t)
# Printing Set Using For Loop.
for i in s:
  print(i)
# You can't change sets like the following. This will give error
# s[0]=5
# print(s)
# This doesn't represent an empty set. 
g={}
print("TYPE 1:",type(g)) # The type you see will be dictionary. 
# This represents an empty set.
g=set() 
print("TYPE 2:",type(g)) # The type you see will be set. 
print("\n")
# Methods Of Set:
s1={1,2,3,4}
s2={2,3,4,5}
print("1st Method Of Union:",s1.union(s2))
s1.update(s2)                            # In this step, s2 will be copied in s1.
print("2nd Method For Union:",s1)        # You can't use this: "s1.update(s2)" directly in print.
print("\n")
print("1st Method Of Intersection:",s1.intersection(s2))
s1.intersection_update(s2)               # In this step, s1 will be updated.
print("2nd Method Of Intersection:",s1)  # You can't use this: "s1.intersection_update(s2)" directly in print.
print("\n")
a1={"Spain","Germany","Brazil","India","Pakistan"}
a2={"England","Spain","Germany","India","Australia"}
print("Symmetric Difference Of Sets:",a1.symmetric_difference(a2))
print("Difference Of Sets:",a1.difference(a2))
print("\n")
print("Disjoint Sets:",a1.isdisjoint(a2))
print("Super Sets:",a1.issuperset(a2))
print("Sub Sets:",a1.issubset(a2))
print("\n")
# USE OF DICTIONARY:
# It gives Output In Order.
di={"Mahad":"Son","Shahnawaz":"Father"}
dic={3057:"Mahad",3041:"Umair"}
print("Accessing All Elements From Dictionary:1",di)
print("Accessing All Elements From Dictionary:2",dic)
print("\n")
print("Accessing All Keys From Dictionary:1",di.keys())
print("Accessing All Keys From Dictionary:1 Using FOR Loop:")
for i in di.keys():
  print(i)
print("Accessing All Values From Dictionary:1",di.values())
print("Accessing All Values From Dictionary:1 Using FOR Loop:")
for z in di.values():
  print(z)
print("\n")
print("Accessing \"Mahad\" From Dictionary:",di["Mahad"]) # If "Mahad" not found, it will give error.
print("Accessing \"Roll Number:3057\" From Dictionary:",dic.get(3057)) # If 3057 not found, it will display "none" not error.
print("Accessing Pairs:",di.items())
print("\n")
# DICTIONARY METHODS:
# In Dictionary, you can't keep keys same each key must be unique.
b1={101:50,102:60,103:70,104:80}
b2={105:90,106:100,107:0}
# b3={}         # This is the way to create empty dictionary.
print("ATTENDANCE 1:",b1)
print("ATTENDANCE 2:",b2)
b1.update(b2)   # Combining the two dictionaries in b1.
print("OVERALL ATTENDANCE:",b1)
# b2.clear      # It will clear b2 dictionary.
# print("CLEAR DICTIONARY:",b2)  # It will give "output={}".
b2.pop(107)     # It will remove pairs from dictionary.
print("DICTIONARY AFTER POP IN ATTENDANCE 2:",b2)
b2.popitem()    # It will remove LAST pair from dictionary.
print("DICTIONARY AFTER POPITEM IN ATTENDANCE 2:",b2)
# del b2        # This deletes the entire dictionary.
print("\n")
# FOR Loop With ELSE:
# ELSE will only execute after completion of FOR Loop not in case of break.
# Else is same for while loop.
for i in range(6):
  print(i)
else:
  print("FOR Loop Is Exited!")
# In the folowing, else will not execute because of break.
for i in range(6):
  print(i)
  if(i==5):
    break
else:
  print("FOR Loop Is Exited!") # This will not work because of break.
print("\n")
# EXCEPTION HANDLING:
# If there is any error in your code, "try and except" will not stop your code but it will print a msg.
try:
  n=int(input("TRY: Enter Any Number: ")) # If you want to use this line before "try", then don't use int.
  for i in range(1,11):
    print(f"MULTIPLICATION OF {n}x{i}={n*i}")
except:
  print("EXCEPTION: There is some error in your code!") 
print("\n")
# You can use more than 1 "except" in your program to specify different errors.
try:
  m=int(input("TRY: Enter Any Index: "))
  b=[4,2]
  print(f"TRY: Number On Index {m} is: {b[m]}")
except ValueError:
  print("EXCEPTION: Number entered is not an integer!")
except IndexError:
  print("EXCEPTION: Index Error!")
print("\n")
# Use Of FINALLY:
# Finally always execute in the program.
# Its main use is in function.
def fun():
  try:
    p=[1,2,3,4]
    v=int(input("TRY: Enter Any Index: "))
    print(p[v])
    return 1
  except:
    print("EXCEPTION: Some Error Occured!")
    return 0
  finally:
    print("FINALLY: I am always executed!")
fun()
# If you not use finally here and just print the statement, it will not work because of return.
# So, the above is the main function of "finally".
print("\n")
# CUSTOM ERRORS:
# Custom Errors stop program from executing and display an error in console.
i=input("CUSTOM ERROR: Enter \"quits\" for no error: ")
if(i=="quits"):
  print("No Error Detected!")
else:
  raise("Some Error Occured!")
print("\n")
# SHORT HAND IF-ELSE:
a=12
b=10
c=9 if a>b else 0 # This means if a>b value of "c" will be 9 else 0.
print("SHORT HAND IF-ELSE:",c)
# ENUMERATE:
# It can be used in list,tuples,strings.
marks=[2,3,4,6,7,8,9,10]
# If you use for loop here you have to increment the index so that's the difference of enumerate.
for i,a in enumerate(marks): # Here "i" represents index while "a" represents marks.
  print("ENUMERATE:",a)
  if(i==7):
    print("HIGHEST MARKS:",a)
print("\n")
# Without "start" indexes starts from 0 while with "start" indexes starts from 1.
for i,a in enumerate(marks,start=1): 
  print("ENUMERATE:",a)
  if(i==7):
    print("HIGHEST MARKS:",a)
print("\n")
# VIRTUAL ENVIRONMENT:
# You can write more than one virtual environments.
# python -m venv "_____"  # You can write any name in dash which will be your virtual environment name.
# The above is the syntax to download virtual environment.
# "_____"\Scripts\activate.bat  # This will activate your virtual environment.
# If you activates virtual environment then, every package will be installed in it instead of global python.
# pip install pandas==1.4 # You can install any version of package through this.
# import pandas as pd  
# pd.__version__   # This will show version of your package.
# If you don't write "as pd" here then, you have to use "pandas.__version__"
# If you write "deactivate" your virtual environment will be closed and global python will be activated.
# "pip freeze" shows all packages installed of one program (VR/GLOBAL PYTHON) at a time.
# "pip freeze > requirements.txt" provides a txt file in which packages are mentioned.
# If you send this txt file to anyone then the receiver should use following command to download the file. 
# "pip install -r requirements.txt" 
# HOW "IMPORT" WORKS:
# import math  # This includes all functions of math.
# import math as m  # Now, you can use m instead of math.
# result=m.sqrt(25) * m.pi
# from math import sqrt,pi  # Now, it only imports sqrt and pi.
# from math import sqrt,pi as p  # Now, you can use p instead of pi.
# print(p)
# from math import *  # This brings each and every thing from math but it is not recommended.
# "dir" will print each and every function and variable of any module on console.
# print(dir(math))
# print(type(math.nan))  # This will print the type of fumction inside math module.
# CREATING OWN MODULE:
# The above topic is available on my phone photos.
# OS MODULE:
# The above topic is mentioned in other program.
# LOCAL Vs GLOBAL Variables:
x=10
# By using "global" you can change global variable inside function otherwise you can't change it.
def my():
  global x
  x=8
  y=5
  print("y=",y)
my()
print("x=",x)
print("\n")
# FILE HANDLING:
# There should be a txt or binary file opened before reading, writing or appending.
# "w" mode directly open or create a file. 
# "w" rewrite the file and removes file previous content.
f=open("ex.txt","w")
f.write("Hello World!")
f.close()
# "a" always writes the content at the end of text.
f=open("ex.txt","a")
f.write(" My name is Mahad Shahnawaz")
f.close()
f=open("ex.txt","r")
text=f.read()
print("Content Of TXT:",text)
f.close()
# If you use "with" you don't have to close file.
with open("ex.txt","a") as f:
  f.write(" I study in FAST NUCES.\n")
with open("ex.txt","r") as f:
  text=f.read()
  print("Content Of TXT:",text)
print("\n")
# The following method prints line by line.
with open("ex.txt","r") as f:
  while True:
    line=f.readline()
    if not line:
      break
    print("READLINE:",line)
# The following method will be useful in many cases.
f=open("ex.txt","a")
lines=["line1","line2","line3"]
for line in lines:
  f.write(line+"\n")
f.close()
# Advanced Functions Of Filing:
with open("ex.txt","r") as f:
  f.seek(5)                # Moves to the 5th byte in file.
  print("TELL FUNCTION:",f.tell())  # Tell function tells that how much you have seeked OR tells your current position. 
  data=f.read(5)           # Read next 5 bytes.
  print("SEEK FUNCTION:",data)
# In above code, if there is no use of "seek" then "read" will read starting 5 characters.
with open("ex.txt","a") as f:  # If you want to use "truncate" always use "a" this mode.
  f.truncate(6)   # It will just show 6 characters in your file and removes the rest.
with open("ex.txt","r") as f:
  print("TRUNCATE FUNCTION:",f.read())