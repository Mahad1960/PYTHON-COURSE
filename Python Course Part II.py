# LAMBDA FUNCTIONS:
# You can also use functions here but lambda is a short cut method. 
square=lambda x:x*x
avg=lambda x,y,z:(x+y+z)/3
print("SQUARE USING LAMBDA:",square(5))
print("AVERAGE USING LAMBDA:",avg(2,4,5))
print("\n")
# MAP, FILTER AND REDUCE:
# Cubing each element of list.
l=[1,2,3,4]
def cube(c):
  return c*c*c
a=list(map(cube,l))  # "list" will convert map into list items.
print("MAP:",a)      # You can use "lambda x:x*x*x" instead of cube in above line.
def fun(b):
    return b>2
new1=list(filter(fun,l))  # Filter only returns True values.
print("FILTER:",new1)
# You must have to import "reduce" in order to use it.
from functools import reduce
sum=reduce(lambda x,y:x+y,l)  # You can use a function here instead of lambda.
print("REDUCE:",sum)  # It works as: [1+2,3,4]=>[3+3,4]=>[6+4]=>[10]
print("\n")
# "IS" Vs "==":
a=5
b=5
print("IS:",a is b)  # Compare identity of objects.
print("==:",a==b)     # Compare Value.
print("\n")
# CLASSES & OBJECTS:
# It is a good practice to keep 1st letter Capital of your class name. 
# It's better to use functions in classes while printing.
class person:
   name="Mahad"
   occupation="Software Developer"
   networth=10000000
   def info(self):            # "SELF" is compulsory here.
      print(f"OBJECT: {self.name} is a {self.occupation}.")
# Self will work for the objects (which can be called multiple times).
a=person()                    # 1st Object
# print("OBJECT:",person.name)          # If you are not using fuction, you can print object like this.
# print("OBJECT:",person.occupation)      
b=person()                    # 2nd Object
b.name="Anfal"                # You can change object information through this.
b.occupation="Doctor"
# print("OBJECT:",b.name,b.occupation)  # If you are not using fuction, you can print object like this.
c=person()                    # 3rd Object
c.name="Simra"                # You can change object information through this.
c.occupation="Doctor"
# print("OBJECT:",c.name,c.occupation)  # If you are not using fuction, you can print object like this.
a.info()
b.info()
c.info()
print("\n")
# CONSTRUCTOR:
# It helps in making objects.
# Constructors use one argument compulsory which is "self".
# The Constructor which takes arguments is a Parametrized Constructor.
# The Constructor which doesn't take arguments is a Default Constructor.
# The following method is the easiest and short cut method to use.
class Person:
  def __init__(self,name,occupation):  # It represents constructer and it will run every time when an object is created.
    self.name=name 
    self.occupation=occupation
  def info(self):
    print(f"CONSTRUCTER: {self.name} is a {self.occupation}.")
a=Person("Mahad","Software Student")
b=Person("Anfal","Medical Student")
a.info()
Person.info(a)   # You can also print information through this.
b.info()
print("\n")
# DECORATORS:
# It modifies the function and return it.
def greet(fx):
  def mfx(*args,**kwargs): # If no arguments required don't use "(*args,**kwargs)" here.
    print("DECORATOR:WELCOME TO THE FUNCTION!")
    fx(*args,**kwargs)     # If no arguments required don't use "(*args,**kwargs)" here.
    print("DECORATOR:THANK U FOR USING THIS FUNCTION!\n")
  return mfx
@greet  # If you doesn't use "greet" here then you should have used "greet(hello)()" in the 86th line.
def hello():
  print("Hello World!")
@greet  # If you doesn't use "greet" here then you should have used "greet(add)(1,2)" in the 87th line.
def add(a,b):
  print("ADDITION:",a+b)
hello()
add(1,2)
# GETTERS & SETTERS:
# You have to use "public variables" for protection and validation without it protection and validation will get lost.
# WITH "PUBLIC VARIABLES":  
class Myclass:
  def __init__(self,n):
    self.__n=n
  def show(self):
    print("SETTER WITH PUBLIC VARIABLE:") 
    print(f"Value Is: {self.__n}\n")
  @property      # This is the syntax to set method for "GETTER".
  def n(self):
    return self.__n
  @n.setter      # This is syntax of applying "Setter".
  def value(self,new_value):
    self.__n=new_value/10
a=Myclass(5)    # In this method "5" will be replaced by "10".
a.value=10      # You have to use function name here to make changes.
a.show()
# WITHOUT "PUBLIC VARIABLES":  
class myclass:
  def __init__(self,n):
    self.n=n    # "n" here should be used for changings.
  def show(self):
    print("SETTER WITHOUT PUBLIC VARIABLE:") 
    print(f"Value Is: {self.n}")
y=myclass(1)
y.n=2           # "n" should be mentioned here to make changes.
y.show()
print("\n")
# INHERITANCE:
class Employee:
  def __init__(self,name,id):
    self.name=name
    self.id=id
  def print(self):
    print(f"The Name Of Employee Is: {self.name} and his/her ID Is: {self.id}.")
# The following step is "Inheritance":
class check(Employee):             # You can use any name here for "class".
  def change(self):
    print("INHERITANCE: This is how inheritance works.")
x=check("Mahad Shahnawaz","3057")  # Now i have use "inheritance" instead of "Employee" here.
x.print()
x.change()
print("\n")
# ACCESS MODIFIERS:
# Public Access Specifier (All the variables and methods are "public" by default in python.)
class practice:
  def __init__(self):
    self.name="Mahad Shahnawaz"
a=practice()
print("PUBLIC:",a.name)
# Private Access Modifier (In python,there is no script of "private" but you can do it by using "__" and it is still achievable.)
class practice:
  def __init__(self):
    self.__name="Mahad Shahnawaz"
a=practice()
# print("PUBLIC:",a.__name)          # Now, it has become "private" by "__" and can't be accessed.
print("PRIVATE:",a._practice__name)  # Now, it has become accessible through indirect method called (Name Mangling).
# Protected Access Modifier (It is done by using "_" but it's important to note that "_" is just a naming convention and doesn't provide any protection.)
class practice:
  def __init__(self):
    self._name="Mahad Shahnawaz"
a=practice()
print("PROTECTION:",a._name)
print("\n")
# STATIC METHODS:
# It is a method that doesn't depend on class or instance data/object. It doesn't need "self".
# You can call it using "class" or "object" name.
class math:
  @staticmethod                        # This is it's syntax.
  def add(x,y):
    return x+y
print("STATIC METHOD:",math.add(5,4))  # 1st Method to print "STATIC METHOD".
m=math()
print("STATIC METHOD:",m.add(4,6))     # 2nd Method to print "STATIC METHOD".
print("\n")
# INSTANCE Vs CLASS VARIABLE:
class check:
  # These two are "class variables".
  company="ENGRO"   # This will be same, everytime it called but you can change it for the individual.
  noofemployee=0
  def __init__(self,name):
    self.name=name
    check.noofemployee+=1
  def show(self):
    print(f"EMPLOYEE {self.noofemployee}: {self.name} is in {self.company}.")
inst1=check("Mahad")
inst1.company="FAUJI FERTILLIZER"   # Here is the changings.
inst1.show()
inst2=check("Shahid")
inst2.show()
inst3=check("Zahid")
inst3.show()
print("\n")
