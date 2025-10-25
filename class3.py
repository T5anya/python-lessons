#LISTS

#Lists are used to store multiple items in a single variable.
thislist = ["apple", "banana", "cherry"]
print(thislist)#['apple', 'banana', 'cherry']

#List items are ordered, changeable, and allow duplicate values.
'''
When we say that lists are ordered, it means that the items have a defined order, and that order will not change.

If you add new items to a list, the new items will be placed at the end of the list.
'''

l1 = [7,9,"harry"] 
l1[0] # 7 
l1[1] # 9 
l1[70]  # error 
l1[0:2] # [7,9]  #list slicing  
l1[0]=8 #unlike strings lists can be changed/mutable

thislist = ["apple", "banana", "cherry"]
print(len(thislist))#3

list1 = ["abc", 34, True, 40, "male"]
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])# cherry

l1 = [1,8,7,2,21,15] 
'''1 l1.sort(): updates the list to [1,2,7,8,15,21] 
2 l1.reverse(): updates the list to [15,21,2,7,8,1] 
3 l1.append(8): adds 8 at the end of the list  [1,8,7,2,21,15,8]
4 l1.insert(3,8): This will add 8 at 3 index [1,8,8,7,2,21,15]
5 l1.pop(2): Will delete element at index 2 and return its value. 
6 l1.remove(21): Will remove 21 from the list.  
3 li.extend'''

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)#['apple', 'banana', "cherry','mango', 'pineapple', 'papaya']
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)#['apple','banana', 'cherry','kiwi','orange']

l1 = [1, 34,62, 2, 6, 11]
value = l1.pop(3)#index
print(value)#2
print(l1)#[1, 34,62, 6, 11]

#Remove the first occurrence of "banana":

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)#['apple', 'cherry', 'banana', 'kiwi']

'''
The clear() method empties the list.

The list still remains, but it has no content.
'''

#join two lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)#['a', 'b', 'c',1,2,3]