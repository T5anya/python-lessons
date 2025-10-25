#TUPLES

#Tuples are used to store multiple items in a single variable.they are unchangeable

a = (1,45,342,3424,False, "Rohan", "Shivam")
print(type(a))#tuple

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])#apple
#indexing and accessing is same as all other data type

a[0]=2 #error a tuple can't be changed

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)#('apple', 'banana', 'cherry', 'orange')

#Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items:

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y) #('banana', 'cherry')

thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists

a = (1, 7, 2) 
'''
1  a.count (1): a count (1) will return number of times 1 occurs in a. 
2  a.index (1) will return the index of first occurrence of 1 in a. '''