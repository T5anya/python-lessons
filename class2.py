#strings

#indexing
name = "Harry"
#The index in a sting starts from 0 to (length -1) in Python. In order to slice a string, we use the following syntax:
#sl=string[inde_start:index_end] the indexing will go to last index-1 means the last index value will not be included in this
nameshort = name[0:3] # start from index 0 all the way till 3 (excluding 3)
print(nameshort)# H a r
character1 = name[1]
print(character1)#a

#negative indexing
name = "Harry"

print(name[0:3])#Har

print(name[-4: -1])#arr
print(name[1:5])#arry

print(name[:4]) # is same as print(name[0:4])#Harr
print(name[1:]) # is same as print(name[1:5])
print(name[1:5])#arry

#SLICING WITH SKIP VALUE 
#We can provide a skip value as a part of our slice like this: 
word = "amazing" 
s=word[1: 6: 2]
print(s) # "mzn" 
#Other advanced slicing techniques: 
Word = "amazing" 
w=Word [:7] 
print(w) # word [0:7] – 'amazing' 
t=Word [0:] 
print(t) # word [0:7] – 'amazing' 

#string functions
a = "Hello, World!"
print(a.upper())# HELLO WORLD
a = "Hello, World!"
print(a.lower())#hello world
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
a = "Hello, World!"
print(a.replace("H", "J"))# Jello World
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
a = "Hello"
b = "World"
c = a + b
print(c)#HelloWorld
d=a+" " +b
print(d)#Hello World
age = 36
#This will produce an error:
txt = "My name is John, I am " + age#error
print(txt)
txt1 = f"My name is John, I am {age}"
print(txt1)
txt2="My name is John, I am "+str(age)
print(txt2)


'''
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isascii()	Returns True if all characters in the string are ascii characters
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning
'''


name = "harry"

print(len(name))#5
print(name.endswith("rry"))#true
print(name.startswith("ha"))#True
print(name.capitalize())#Harry

a = 'Harry is a good boy\nbut not a bad \'boy\''


print(a)
# Expected output:
# Harry is a good boy
# but not a bad 'boy'


