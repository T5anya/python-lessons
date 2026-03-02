#ERRORS
#Errors occur due to mistakes in the code that prevent it from running. These can be syntax errors or logical errors6

#SYNTAX ERROR

#print("Hello World" This will cause a syntax error because of the missing closing parenthesis

#INDENTATION ERROR

#def my_function():
# print("Hello World") This will cause an indentation error because the print statement is not indented properly

#EXCEPTION HANDLING
#Exceptions are errors that occur during the execution of a program. They can be handled using try-except blocks to prevent the program from crashing.

a=int(input("Enter a number: "))
try:
    result=10/a
    print("The result is:",result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
else:
    print("The division was successful.")
#if no exception occurs, this block will be executed
finally:
    print("This block will always be executed.")#run always no matter what

#FILE HANDLING-

#File handling means Creating, Reading, Updating,
#Deleting(CRUD) operations that we can perform in files9
#Now lets see how to perform these operations in python.
#We have to use open() function to open a file in python.
#Now there are multiple modes to open the file.

#file modes-

#'r' - Read mode (default) - Opens a file for reading. If the file does not exist, it raises a FileNotFoundError.
#'w' - Write mode - Opens a file for writing. If the file already exists, it truncates the file to zero length. If the file does not exist, it creates a new file.
#'a' - Append mode - Opens a file for appending. If the file already exists, it appends the new data to the end of the file. If the file does not exist, it creates a new file.
#'x' - Exclusive creation mode - Opens a file for exclusive creation. If the file already exists, it raises a FileExistsError. If the file does not exist, it creates a new file.
#'b' - Binary mode - Opens a file in binary mode. This is used for non-text files like images or videos.

with open(r"C:\Users\tanya\OneDrive\Desktop\coding\python\D.txt", "r") as file:
    content = file.read()
    print(content)  

with open(r"C:\Users\tanya\OneDrive\Desktop\coding\python\D.txt", "w") as file:
    file.write("This is a new line in the file.")
    #print(file.read())#This will cause an error because the file is opened in write mode, which does not allow reading.

with open(r"C:\Users\tanya\OneDrive\Desktop\coding\python\D.txt", "r") as file:
    content = file.read()
    print(content)  
file.close()
