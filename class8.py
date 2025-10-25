#LOOPS

#WHILE
#while (condition):  The block keeps executing until the condition is true  Body of the loop 
import random

num = random.randint(1,10)

tries = 0

while True:
    guess = int(input("please guess your number between 1 and 10 :- "))
    if num == guess:
        tries +=1
        print(f"you are right you guessed the number is {tries} tries")
        break

    elif num < guess:
        print("go a little lower")
        tries +=1
    
    elif num > guess:
        print("go a little higher")
        tries +=1

    else:
        tries +=1 
        print("sorry you are wrong")

print(12)

l = [1, "Harry", False, "This", "Rohan", "Shubham", "Shubhi"]

i = 0

while(i<len(l)):
    print(l[i])
    i +=1
'''
output-
1
Harry
False
This
Rohan
Shubham
Shubhi
'''
#with the break statement we can stop the loop even if the while condition is true:
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
'''
output-
1
2
3

'''
#With the continue statement we can stop the current iteration, and continue with the next:
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
'''
output-
1
2
4
5
6
'''


#FOR

# range(start, stop, step)

for i in range(4):
    print(i) # prints 1  2  3

l = [1, 7, 8] 
for item in l: 
    print(item) # prints 1, 7 and 8

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 
  if x == "banana":
    break
#prints apple    banana


l= [1,7,8] 
for item in l: 
    print(item) 
else: 
    print("done") # this is printed when the loop exhausts! 
'''
Output: 
1 
7 
8 
done '''

l = [1,7,8] 
for item in l: 
    pass          
# without pass, the program will throw an error

#palindrome num

a = "NAMAN"

b = ""
for i in range(len(a)-1,-1,-1):
   b = b + a[i]


if b == a:
   print("your string is pallindrome")

else:
   print("its not a pallindrome")