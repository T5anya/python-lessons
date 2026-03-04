#encapsulation-Encapsulation is the process of hiding the internal details of an object and only exposing a public interface.
#Encapsulation means putting data (variables) and code (functions)together in one place — inside a class
# It also means hiding the internal details of how things work, and only showing what is needed

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private variable
    def get(self):
        return self.__balance
    def deposit(self, amount):
        self.__balance += amount
    def get_balance(self):
        return self.__balance
account = BankAccount(1000)
print(account.get())  # Output: 1000
account.deposit(500)
print(account.get_balance())  # Output: 1500
# print(account.__balance)  # This will raise an AttributeError because __balance is private

#access modifiers-Access modifiers means how we give access of our attributes and methods
# to the object or inherited classes. There are 3 types lets see them one by one.

#1. Public: Public members are accessible from anywhere in the program. They can be accessed by any object or class.
#2. Protected: Protected members are accessible within the class and its subclasses. They are denoted by a single underscore (_) before the member name.
#3. Private: Private members are accessible only within the class. They are denoted by a double underscore (__) before the member name.

class demo:
    def __init__(self):
        self.public_var = "I am public"
        self._protected_var = "I am protected"
        self.__private_var = "I am private"
    def show(self):
        print(self.public_var)
        print(self._protected_var)
        print(self.__private_var)
d1 = demo()
print(d1.public_var)  # Output: I am public
print(d1._protected_var)  # Output: I am protected
#print(d1.__private_var)  # This will raise an AttributeError because __private_var is private

#you can also make methods private by using double underscore before the method name.

#ABSTRACTION-

#Abstraction is used to simplifying complex systems by focusing on essential features and hiding unnecessary details;
#Abstract classes are classes that contains one or more abstract methods;

from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
c2=Rectangle(5, 10)
print(c2.area())  # Output: 50

#DUNDER METHODS-
#Dunder methods are special methods in Python that start and end with double underscores
#,like __init__, __str__, __add__, etc They automatically get called when you perform 
#certain actions on an object

#DECORATERs-
#B A decorator is just a function that modifies another function without changing its 
#actual code.Imagine you have a cake (your function). A decorator is like putting icing 
#on the cake. It doesn’t change the cake itself, but makes it better, prettier, or adds 
#some new flavor

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper
@my_decorator
def say_hello():
    print("Hello!") 
say_hello()


#ARGS and KWARGS-
# *args allows you to pass a variable number of non-keyword arguments to a function, 
#while **kwargs allows you to pass a variable number of keyword arguments to a function.
# They’re special keywords in Python used in function definitions to accept a flexible number of arguments%
# Now you always don’t have to use Args and Kwargs the main thing is * , ** you can use any names in front of them.
# so *args are used for multiple positional arguments, and **kwargs are used for multiple key word arguments.
# And the *args becomes a tuple and **kwargs becomes a dictionary

def function(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)
function(1, 2, 3, name="Alice", age=30)

#LIST DICTONARY SETS COMPREHENSION-
#List comprehension is a concise way to create lists. It consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses.

squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
LABELS=["EVEN" if x%2==0 else "ODD" for x in range(10)]
print(LABELS)  # Output: ['EVEN', 'ODD', 'EVEN', 'ODD', 'EVEN', 'ODD', 'EVEN', 'ODD', 'EVEN', 'ODD']

evens={x for x in range(10) if x%2==0}
print(evens)  # Output: {0, 2, 4, 6, 8}
even={x:x**2 for x in range(10) if x%2==0}
print(even)  # Output: {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

uniqueevennumbers={x*x for x in range(10) if x%2==0}
print(uniqueevennumbers)  # Output: {0, 4, 16, 36, 64}

#lambda function-
#A lambda function is a small anonymous function that can take any number of arguments,
#but can only have one expression. It is often used for short, simple functions that 
# are not worth defining with a full function definition.
add = lambda x, y: x + y
print(add(5, 3))  # Output: 8

check_even=lambda x:x%2==0
print(check_even(4))  # Output: True

#Map function applies a given function to each item of an iterable (like a list) and returns a map object (which is an iterator). You can convert the map object to a list or other iterable type.
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x**2, numbers)
print(list(squared))  # Output: [1, 4, 9, 16, 25]

#filter function constructs an iterator from elements of an iterable for which a function returns true. It is used to filter the elements of an iterable based on a condition.
numbers = [1, 2, 3, 4, 5]
even_numbers=filter(lambda x:x%2==0, numbers)
print(list(even_numbers))  # Output: [2, 4]


#SIMPLE BANK MANAGEMENT SYSTEM
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient Balance")
        else:
            self.__balance -= amount
            print("Withdrawn:", amount)

    def show_balance(self):
        return f"Current Balance: {self.__balance}"
account = BankAccount("Alice", 1000)
print(account.show_balance())  # Output: Current Balance: 1000
account.deposit(500)  # Output: Deposited: 500
print(account.show_balance())  # Output: Current Balance: 1500
account.withdraw(200)  # Output: Withdrawn: 200
print(account.show_balance())  # Output: Current Balance: 1300
