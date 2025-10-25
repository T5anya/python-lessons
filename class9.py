#FUNCTIONS

'''
A function is a group of statements performing a specific task. 
When a program gets bigger in size and its complexity grows, it gets difficult for a 
program to keep track on which piece of code is doing what!

yntax 
def func1(): 
print('hello')
'''

def avg():
    a = int(input("Enter your number: "))
    b = int(input("Enter your number: "))
    c = int(input("Enter your number: "))
    
    average = (a + b + c)/3
    print(average)

#To call a function, write its name followed by parentheses:

avg()

#FUNCTIONS WITH RETURN STATEMENT AND ITS DIFFERENCE FROM PRINT STATEMENT

def greet():
    print ("hello user")
greet()

def greet():
    return ("hello user")
print(greet())

'''
There are two types of functions in python: 
• Built in functions (Already present in python) 
• User defined functions (Defined by the user) 
Examples of built in functions includes len(), print(), range() etc. 
The greet()/avg() function we defined is an example of user defined function.
'''

#ARGUMENTS AND PARAMETERS 
'''
Information can be passed into functions as arguments.

Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.'''

def greet(name):
    print ("hello"+ name)
greet()

'''
A parameter is the variable listed inside the parentheses in the function definition.

An argument is the actual value that is sent to the function when it is called.

def my_function(name): # name is a parameter
  print("Hello", name)

my_function("Emil") # "Emil" is an argument

f your function expects 2 arguments, you must call it with exactly 2 arguments.

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

'''

#DEFAULT PARAMETER

#You can assign default values to parameters. If the function is called without an argument, it uses the default value:

def my_function(name = "friend"):
    print("Hello",+ name)

my_function("Email")
my_function()

'''
Hello Email
Hello friend
'''

#TYPES OF ARGUMENTS
#three types
#KEYWORD ARGUMENTS
# with keyword arguments, the order of the arguments does not matter.

def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(name = "Buddy", animal = "dog")
'''
I have a dog
My dog's name is Buddy
'''

#POSITIONAL ARGUMENTS 
#Positional arguments must be in the correct order:

def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("dog", "Buddy")
'''
I have a dog
My dog's name is Buddy
'''

#switching the order can change results:

my_function("buddy", "dog")

'''
I have a buddy
My dog's name is dog
'''

#DEFUALT ARGUMENT U HAVE STUDIED ABOVE 

#RECURSION

'''
Recursion is a function which calls itself. 
It is used to directly use a mathematical formula as function
'''

'''
factorial(0) = 1
factorial(1) = 1
factorial(2) = 2 X 1
factorial(3) = 3 X 2 X 1
factorial(4) = 4 X 3 X 2 X 1
factorial(5) = 5 X 4 X 3 X 2 X 1
factorial(n) = n X n-1 X......3 X 2 X 1

factorial(n) = n * factorial(n-1)
'''

def factorial(n):
    if(n==1 or n==0):
        return 1
    return n * factorial(n-1)


n = int(input("Enter a number: "))
print(f"The factorial of this number is: {factorial(n)}")

def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)
n=int(input("enter a number"))
fibonacci(n)


#scope
'''
A variable is only available from inside the region it is created. This is called scope.

Local Scope-
A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.

def myfunc():
  x = 300
  print(x)

myfunc()
here x is a local variable

Global Scope-
A variable created in the main body of the Python code is a global variable and belongs to the global scope.

x = 300

def myfunc():
  print(x)

myfunc()

print(x)
here x is a global variable

'''



