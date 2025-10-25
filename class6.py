#SETS

#Set is a collection of non-repetitive elements. it is unordered
s = set()    # Dont use s = {} as it will create an empty dictionary       
# no repetition allowed! 
s.add(1) 
s.add(2)           
# or set ={1,2} 
#True and 1 is considered the same value:
#False and 0 is considered the same value:
w = {1, 5, 32, 54,5, 5, 5} 


print(w)#{32,1,5,54} 
#it's order can change and one value will come one time only 
'''
len(s): Returns 4, the length of the set  
s.remove(8): Updates the set s and removes 8 from s. 
s.pop(): Removes an arbitrary element from the set and return the element 
removed. 
s.clear():empties the set s. 
s.union({8,11}): Returns a new set with all items from both sets. {1,8,2,3,11}. 
s.intersection({8,11}): Return a set which contains only item in both sets  {8}.

'''
s1 = {1, 45, 6, 78}  
s2 = {7, 8, 1, 78}

print(s1.union(s2)) # {1, 45, 6, 78 ,7, 8,}

print(s1.intersection(s2)) # {1,78}