#OOPS(OBJECT ORIENTED PROGRAMMING SYSTEM)

#Python is an object-oriented language, allowing you to structure your code using classes and objects for better organization and reusability.

#1. Class: A class is a blueprint for creating objects. It defines a set of attributes and methods that the objects created from the class will have.
#2. Object: An object is an instance of a class. It is created using the class and can have its own unique values for the attributes defined in the class.
#When you create an object from a class, it inherits all the variables and functions defined inside that class.

from enum import unique
import numbers
from os import name


class MyClass:
  x = 5#attribute
  def hello():
    print("Hello, World!")#method

p1=MyClass()#creating an object
print(p1.x)#accessing attribute
MyClass.hello()#accessing method

#class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.

#The __init__() function is a special method that is called when an object is instantiated. It is used to initialize the attributes of the class.
#constructor
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("Name:", self.name)
        print("Marks:", self.marks)

s1 = Student("Tanya", 95)
s2 = Student("Rohit", 88)   

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car: {self.year} {self.make} {self.model}")
car1 = Car("Toyota", "Camry", 2020)
car1.display_info() 
car2 = Car("Honda", "Civic", 2019)
car2.display_info()

# we can also set default value in __init__() method

class Car:
    def __init__(self, make, model, year=2020):
        self.make = make
        self.model = model
        self.year = year
car1 = Car("Toyota", "Camry")
print(car1.year)  # Output: 2020
car2 = Car("Honda", "Civic", 2019)
print(car2.year)  # Output: 2019

#Without the __init__() method, you would need to set properties manually for each object:
#Using __init__() makes it easier to create objects with initial values

#It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any method in the class:

class Person:
  def __init__(myobject, name, age):
    myobject.name = name
    myobject.age = age

  def greet(abc):
    print("Hello, my name is " + abc.name)

p1 = Person("Emil", 36)
p1.greet()

#You can add new properties to existing objects:

class Person:
  def __init__(self, name):
    self.name = name

p1 = Person("Tobias")

p1.age = 25
p1.city = "Oslo"

print(p1.name)
print(p1.age)
print(p1.city)

#ATTRIBUTES
#Attributes are variables that belong to an object. They are used to store information about the object. You can access and modify attributes using dot notation.
class Person:
    wheel = 4 #class attribute
    def __init__(self, name, age):
        self.name = name#  instance attribute
        self.age = age#  instance attribute

p1 = Person("Alice", 30)
print(p1.name)  # Output: Alice

#methods
#Methods are functions that belong to an object. They are used to perform actions on the object or to retrieve information about the object. You can call methods using dot notation.

class animal:
    def __init__(self, age):
        self.age = age
    def show(self):
      print("This is an animal of age", self.age)#instance method
    @staticmethod
    def info():
        print("Animals are living beings")#static method
    
    @classmethod
    def class_info(cls):
        print("This is the animal class age of {self.age}")#class method
a1 = animal(12)
a1.show()  # Output: This is an animal of age 12  
a1.info() # Output: Animals are living beings
a1.class_info() # animal has no attribute age, so it will give an error

#a class can have multiple methods, and you can call them on the same object:

#INHERITANCE

#Inheritance allows us to define a class that inherits all the methods and properties from another class.
#Parent class is the class being inherited from, also called base class.
#Child class is the class that inherits from another class, also called derived class.

class Parent:
    def parent_method(self):
        print("This is a method in the parent class.")  
class Child(Parent):
    def child_method(self):
        print("This is a method in the child class.")
c1 = Child()
print(c1.parent_method())  # Output: This is a method in the parent class.
print(c1.child_method())  # Output: This is a method in the child class.

#Now the inherited class has all the powers of parent class that means all the methods, 
# attributes can be accessed by the instance of child class as well.

#constructor in inheritance
class Parent:
    def __init__(self, name):
        self.name = name
class Child(Parent):
    def display(self):
        self.name = name
c1=Child("Alice")
print(c1.name)  # Output: Alice

#super() function is used to call the constructor of the parent class from the child 
# class. It allows you to access the methods and properties of the parent class.

class Parent:
    def __init__(self, name):
        self.name = name
    def show(self):
        print(f"this is {self.name},{self.age}")    
class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Call the constructor of the parent class
        self.age = age
c1 = Child("Alice", 30)
c1.show()

#types of inheritance
#1. Single Inheritance: A child class inherits from a single parent class.
#2. Multiple Inheritance: A child class inherits from multiple parent classes.

class Parent1:
    def method1(self):
        print("This is method 1 from Parent1.")
class Parent2:
    def method2(self):
        print("This is method 2 from Parent2.")
class Child(Parent1, Parent2):
    def child_method(self):
        print("This is a method in the child class.")
c1 = Child()
c1.method1()  # Output: This is method 1 from Parent1.
c1.method2()  # Output: This is method 2 from Parent2.

#3. Multilevel Inheritance: A child class inherits from a parent class, which in turn inherits from another parent class.
#grandparent class → parent class → child class

class Grandparent:
    def grandparent_method(self):
        print("This is a method in the grandparent class.")
class Parent(Grandparent):
    def parent_method(self):
        print("This is a method in the parent class.")
class Child(Parent):
    def child_method(self):
        print("This is a method in the child class.")
c1 = Child()
c1.grandparent_method()  # Output: This is a method in the grandparent class.
c1.parent_method()       # Output: This is a method in the parent class.    
c1.child_method()        # Output: This is a method in the child class.


#project-

class factory:
    def __init__(self,material,zips):
        self.material = material
        self.zips = zips
    def show(self):
        print(f"this is a factory of {self.material} and it produces {self.zips} zips")
class bhopalfactory(factory):
    def __init__(self,material,zips,color):
        super().__init__(material,zips)
        self.color = color
    def show(self):
        print(f"this is a factory of {self.material} and it produces {self.zips} zips and it is located in {self.color}")
class punefactory(bhopalfactory):
    def __init__(self,material,zips,color,pockets):
        super().__init__(material,zips,color)
        self.pockets = pockets
    def show(self):
        print(f"this is a factory of {self.material} and it produces {self.zips} zips and it is located in {self.color} and it has {self.pockets} pockets")

#POLYMORPHISM-Same method name, different behavior.
# Polymorphism allows us to define methods in the child class with the same name as methods in the parent class.

class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  x.move()

#method overriding

class Parent:
    def show(self):
        print("This is a method in the parent class.")
class Child(Parent):
    def show(self):
        print("This is a method in the child class.")
c1 = Child()
c1.show()  # Output: This is a method in the child class.

#inheritance and polymorphism together

class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()

