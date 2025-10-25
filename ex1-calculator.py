num1=int(input("enter our first number"))
num2=int(input("enter our second number"))
result=0
print(
    '''
    1 for addition
    2 for subtraction
    3 for multiplication
    4 for divison
    5 for remainder
'''
)
ch=int(input("enter ur choice"))
if ch==1:
    result=num1+num2
    print(result)
elif ch==2:
    result=num1-num2
    print(result)
elif ch==3:
    result=num1*num2
    print(result)
elif ch==4:
    result=num1/num2
    print(result)
elif ch==5:
    if num1>num2:
        result=num1%num2
        print(result)
    else:
        result=num2%num1
        print(result)
else:
    print("Invalid choice")