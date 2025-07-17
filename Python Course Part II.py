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
# CLASS METHODS:
class check:
  company="Apple"
  def show(self):
    print(f"My name is {self.name} and the company is {self.company}.")
  @classmethod  # This decorator will change the company name for all instances but without it only one instance will change.
  def change_company(cls,new_company):  # You can use any word in place of "cls".
    cls.company=new_company
x=check()
x.name="Mahad"
x.show()
x.change_company("Tesla")
x.show()
x1=check()
x1.name="Rizwan"
x1.show()
print("\n")
# CLASS METHODS Vs ALTERNATIVE CONSTRUCTORS:
class constructor:
  def __init__(self,name,age):
    self.name=name
    self.age=age
  @classmethod
  def str(cls,string):
    name,age=string.split(",")
    return cls(name,int(age))   # If you don't mention "int" here, age will be considered as string.
n=constructor.str("Mahad,20")
print("ALTERNATIVE CONSTRUCTOR:",n.name,n.age)
print("\n")
# dir() , __dict__ , help() METHODS:
z=[1,2,3]                    # You can also use it as tuple.
print("METHODS:",dir(z))     # It will tell all methods of "list".
print("\n")
print("SPECIFIC METHOD RESEARCH:",z.__add__)  # "__add__" is a method of list, this syntax will tell how this method works.
print("\n")
class dic:
  def __init__(self,name,age):
    self.name=name
    self.age=age
o=dic("Mahad",20)
print("\n")
print("CLASS IN DICT FORM:",o.__dict__)       # It will print the class in dictionary form.
print("\n")
# "HELP" Method is used to get help documentation for an object, including description of its attributes and methods.
print(help(dic))
print("\n")
# SUPER KEYWORD:
class Parent:
  def parent_method(self):
    print("This is parent method.")
class Child(Parent):
  def parent_method(self):
    print("Mahad.")
    super().parent_method()   # This will get "parent method" from above.
  def child_method(self):
    print("This is child method.")
    super().parent_method()   # This will get "parent method" in "child method".
child_object=Child()
child_object.child_method()
child_object.parent_method()
print("\n")
# Using "SUPER" For Constructor:
class parent:
  def __init__(self,name,age):
    self.name=name
    self.age=age
class child(parent):
  def __init__(self,name,age,lang):
    super().__init__(name,age)
    self.lang=lang
object=child("Mahad","20","Urdu")
print("SUPER:",object.name)
print("SUPER:",object.age)
print("SUPER:",object.lang)
print("\n")
# MAGIC / DUNDER METHODS:
# They start with "__".
# You can study it futher on GOOGLE.
class emp:
  def __init__(self,name):
    self.name=name
  def __str__(self):   # Human Readable.
    return f"STR: The name of employee is {self.name}."
  def __repr__(self):  # Developer / Debug Format.
    return f"REPR: Employee('{self.name}')"
  def __call__(self):
    print("CALL: HEY! I am Good.")
e=emp("Mahad")
print(str(e))
print(repr(e))
e()  # For Call Method.
print("\n")
# OPERATOR OVERLOADING:
# You can study it futher on GOOGLE.
class Vector:
  def __init__(self,i,j,k):
    self.i=i
    self.j=j
    self.k=k
  def __str__(self):
    return f"{self.i}i + {self.j}j + {self.k}k"
  def __add__(self,x):
    return Vector(self.i + x.i, self.j + x.j, self.k + x.k)  # By using "return vector" the original type "string" will be changed to "vector".  
v1=Vector(3,4,5)
print("VECTOR 1:",v1)
v2=Vector(6,7,8)
print("VECTOR 2:",v2)
print("VECTOR ADDITION:",v1+v2)
print("TYPE OF VECTOR:",type(v1+v2))
print("\n")
# SINGLE INHERITANCE: (MOST COMMON)
class Animal:
  def __init__(self,name,specie):
    self.name=name
    self.specie=specie
  def sound(self):
    print(f"{self.name} makes sound.")
class Dog(Animal):
  def __init__(self,name,specie,breed):
    super().__init__(name,specie)
    self.breed=breed
  def noise(self):
    print(f"SINGLE INHERITANCE: {self.name}, the {self.breed} Dog barks.")
v=Dog("BOOGY","Famous","German Shepherd")
v.noise()
# MULTIPLE INHERITANCE:
# In this class only one child with multiple parents.
class music:
  def __init__(self,name):
    self.name=name
class dance:
  def __init__(self,style):
    self.style=style
class both(music,dance):
  def __init__(self,name,style):  # This is the method to call multiple parents in child class.
    music.__init__(self,name)
    dance.__init__(self,style)
  def __str__(self):
    return f"MULTIPLE INHERITANCE: {self.name} is a {self.style} Dancer."
now=both("Shahrukh","Break")
print(now)
print("\n")
print("MRO:",both.mro())  # "mro" tells which will run first in class.
print("\n")
# MULTILEVEL INHERITANCE:
class Animal:
    def __init__(self, name):
        self.name = name
    def sound(self):
        print(f"MULTILEVEL INHERITANCE: {self.name} makes sound.")
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    def speak(self):
        print(f"MULTILEVEL INHERITANCE: The {self.breed} breed {self.name} barks.")
class Puppy(Dog):
    def __init__(self, name, breed, color):
        super().__init__(name, breed)
        self.color = color
    def bark(self):
        print(f"MULTILEVEL INHERITANCE: {self.color} color {self.breed} barks.")
p = Puppy("Doggy", "German Shepherd", "White")
p.sound()   # From Animal
p.speak()   # From Dog
p.bark()    # From Puppy
print("\n")
# HYBRID & HIERARCHICAL INHERITANCE:
# "Hybrid inheritance" is a combination of multiple & multilevel inheritance.
class ani:
    def __init__(self, n):
        self.n = n
    def eat(self):
        print(f"HYBRID INHERITANCE: {self.n} eats food.")
class do(ani):
    def __init__(self, n, b):
        ani.__init__(self, n)  
        self.b = b
    def ba(self):
        print(f"HYBRID INHERITANCE: {self.b} barks.")
class Bird(ani):
    def __init__(self, n, c):
        ani.__init__(self, n)
        self.c = c
    def fly(self):
        print(f"HYBRID INHERITANCE: {self.n} of {self.c} doesn't fly.")
class Flying(do, Bird):
    def __init__(self, n, b, c, health):
        do.__init__(self, n, b)     
        Bird.__init__(self, n, c) 
        self.health = health
    def sh(self):
        print(f"HYBRID INHERITANCE: {self.n} has a {self.c} color which is {self.b} breed and {self.health}.")
f = Flying("BILLU", "German Shepherd", "Black", "Healthy")
f.sh()
# In "Hierarchical Inheritance", multiple child classes inherit from a single parent.
class An:
  def __init__(self,name):
    self.name=name
  def speak(self):
    print(f"HIERARCHICAL INHERITANCE: {self.name} makes a sound.")
class d(An):
  def __init__(self, name,col):
    super().__init__(name)
    self.col=col
  def bark(self):
    print(f"HIERARCHICAL INHERITANCE: {self.name} of {self.col} color barks.")
class C(An):
  def __init__(self, name,col):
    super().__init__(name)
    self.col=col
  def meow(self):
    print(f"HIERARCHICAL INHERITANCE: {self.name} of {self.col} color meows.")
obj1=d("Doggu","Brown")
obj1.bark()
obj2=C("Catu","White")
obj2.meow()  # This will not work alone because you haven't give color, so for this you have to call "d" first.
print("\n")
# TIME MODULE:
import time
def for_loop():
  for i in range(1,11):
    print(i)
def while_loop():
  i=1
  while i<=10:
    print(i)
    i=i+1
initial=time.time()
for_loop()
print("TIME TAKEN FOR {FOR LOOP}:",time.time()-initial)
initial=time.time()
while_loop()
print("TIME TAKEN FOR {WHILE LOOP}:",time.time()-initial)
print("\n")
time.sleep(3)
print("TIME SLEEP: This sentence is printed after 3 seconds.")
t=time.localtime()   # It tells the local time of that city where are you present.
print("LOCAL TIME:",t)
print("\n")
# WARLUS OPERATOR:
a=True
print("WARLUS OPERATOR:",a:=False)  # If you write "print(a=False)", this will give error.  
foods=list()
while (food:=input("Which color do you like? ")) !="quit":  # This will stop taking input when "quit" will typed.
  foods.append(food)
print("WARLUS OPERATOR:",foods)
print("\n")
# GENERATORS:
# You can create a "Generator" using "yield" statement.
# "Generators" doesn't store values. It generate values on the fly.
def my_generator():
  for i in range(1,6):
    yield i                    # For "Generators", "yield" keyword is used.
gen=my_generator()
# 1st Method: 
print("GENERATOR:",next(gen))  # "next" keyword runs the code until it reaches the next yield.
print("GENERATOR:",next(gen))  # It will print one value at a time so if you want 5 values you have to write this statement 5 times.
print("\n")
# 2nd Method:                  # This method will work like a "for" loop.
# for i in gen:
#   print("GENERATOR:",i)
# FUNCTION CACHING:
# It is done by "FUNCTOOL Module".
# It's complete use has been done in other file, you can see it.
# REGULAR EXPRESSIONS:
# It is done by "Re Module".
# It's complete use has been done in other file, you can see it.
# ASYNC IO:
# It is done by "Asyncio Module".
# It's complete use has been done in other file, you can see it.
# MULTITHREADING:
# It is done by "Threading Module", "Concurrent Module".
# It's complete use has been done in other file, you can see it.
# MULTIPROCESSING:
# It is done by "Multiprocessing Module".
# It's complete use has been done in other file, you can see it.
