print("A")
print("b")
print("c",end="")
print("d",end="")
#using end in c and d print will avoid a new ine and output will be-
'''
A
b
cd

'''

#variables
a = 1

b = 2

c = 7

name = "harry"

print(a + b)

#datatypes


a = 1 # a is an integer

b = 5.22 # b is a floating point number

c = "Harry" # c is a string

d = False # d is a boolean variable

e = None # e is a none type variable


#rules_variables
a = 23

aaa = 435

harry = 34

sameer = 45

_samerr = 34

# @sameer = 56 # Invalid due to @ symbol
# s@meer # Invalid due to @ symbol

#operaters

# Arithmetic Operators
a = 7
b = 4
c = a + b
print(c)

# Assignment Operators
a = 4-2 # Assign 4-2 in a
print(a)
b = 6
# b += 3 # Increment the value of b by 3 and then assign it to b
b -= 3 # Decrement the value of b by 3 and then assign it to b
print(b)

# Comparison Operators

d = 5==5

print(d)


# Logical Operators

e = True or False

# Truth table of 'or' 
print("True or False is ", True or False)
print("True or True is ", True or True)
print("False or True is ", False or True)
print("False or False is ", False or False)

# Truth table of 'and' 
print("True and False is ", True and False)
print("True and True is ", True and True)
print("False and True is ", False and True)
print("False and False is ", False and False)

print(not(True))

#membership operator

fruits = ["apple", "banana", "cherry"]
print("banana" in fruits) # True
print("pineapple" not in fruits) # True

#identity operator

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z) # True
print(x is y) # False
print(x == y) # True
print(x is not y) # True

#types

a = "31.2"
b = float(a) # a but the type should be float
t = type(b) 

print(t)

#inputs
a = int(input("Enter number 1: "))#Variables are containers for storing data values. here a is a variable

b = int(input("Enter number 2: "))

print("Number a is: ", a)
print("Number b is: ", b) 
print("Sum is ", a + b)

# comments on python symbol, and Python will ignore everything 
#  # on that line: 
# This is a comment
#for multiline comments
#use '''

""" 
This is a comment 
written in 
more than just one line 
"""

'''int(): Converts a value to an integer. Example: int("123") → 123.

float(): Converts a value to a floating-point number. Example: float("12.34") → 12.34.

complex(): Converts real and imaginary parts to a complex number. Example: complex(1, 2) → (1+2j).

String Conversions

str(): Converts a value to a string. Example: str(123) → "123".

Boolean Conversion

bool(): Converts a value to a Boolean (True or False). Example: bool(0) → False.

Sequence Conversions

list(): Converts an iterable (e.g., string, tuple) to a list. Example: list("abc") → ['a', 'b', 'c'].

tuple(): Converts an iterable to a tuple. Example: tuple([1, 2, 3]) → (1, 2, 3).

set(): Converts an iterable to a set (removes duplicates). Example: set("aabbcc") → {'a', 'b', 'c'}.

Dictionary Conversion

dict(): Converts a sequence of key-value pairs (e.g., tuples) to a dictionary. Example: dict([('a', 1), ('b', 2)]) → {'a': 1, 'b': 2}.

ASCII and Unicode Conversions

chr(): Converts a Unicode code point to its corresponding character. Example: chr(65) → 'A'.

ord(): Converts a character to its Unicode code point. Example: ord('A') → 65.

Binary, Octal, and Hexadecimal Conversions

bin(): Converts an integer to its binary representation. Example: bin(10) → '0b1010'.

oct(): Converts an integer to its octal representation. Example: oct(10) → '0o12'.

hex(): Converts an integer to its hexadecimal representation. Example: hex(10) → '0xa'.'''

a="harry"#string
i=int(a)#integer
