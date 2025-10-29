# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode

import random
ch=int(input("Enter 1 to Code and 2 to Decode:"))
if ch==1:
    msg=input("enter the message to be coded:")
    words=msg.split(" ")
    coded_words=[]
    for word in words:
        if len(word)>=3:
            first_letter=word[0]
            rest_word=word[1:]
            new_word=rest_word+first_letter
            finalcode_word='abc'+new_word+'xyz'
            coded_words.append(finalcode_word)
            print("Coded message is:", coded_words)
        else:
            reversed_word=word[::-1]
            coded_words.append(reversed_word)
            print("Coded message is:", coded_words)
elif ch==2:
    msg=input("enter the message to be decoded:")
    words=msg.split(" ")
    coded_words=[]
    for word in words:
        if len(word)>=3:
            word1=word[3::]
            word_final=word1[:-3]
            last_letter=word_final[-1]
            rest_word=word_final[0:len(word_final)-1:1]
            new_word=last_letter+rest_word
            coded_words.append(new_word)
            print("Coded message is:", coded_words)
        else:
            reversed_word=word[::-1]
            coded_words.append(reversed_word)
            print("Coded message is:", coded_words)
else:
    print("Enter Correct Choice")
  
