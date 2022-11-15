

# Python try except finally blocks
# The try block lets you test the block of code for errors
# The except block lets you handle the error
# The finallu block lets you execute the code, regardless of the result of the try and except
# blocks
# Exception handling
# when an error occurs , or an exception as we call it,Python will normally stop and 
# generate an error message These exceptions can handle using the try statement

# The try block generate an exception, because x is not defined
try:
    print(x)
except:
    print('an exception occured')

# Since the try block raises an error, the except block will be executed 
# without the try block, the program will crash and raise an error
# This statement will raise an error, because x is not defined
print(x)

#Many exceptions
# you can define as many exception blocks as you want , if you want special block of code for
# kind of an error 

# print one message if the try block raises a NameError and other block for other errors
try:
    print(x)
except NameError:
    print('variable is not defined')
except:
     print('somethingelse went wrong')


# you can use else keyword to define a block of code to be executed if no errors were raised
# Example
# IN this try block does not generate any error
try:
    print("hello")
except:
    print('something went wrong')
else:
    print('Nothing went wrong')

# Finally
# The finally block, if specified, will be executed regardless if the try block raises an error or not 

try:
    print(x)
except:
    print('something went wrong')
finally:
    print('The try except finished')

# this can be used to close objects and clean up resources
# try to open a file and write to a file that is not writable
try:
    f = open('demofile.txt')
    f.write("Lorum Ipsum")
except:
    print('something went wrong writing to the file')
finally:
    f.close()


# Python command line input
# Python allows for command line input
# that means we are able ask user for input
print('Enter your name:')
x = input()
print('hello', x)

y = input("enter your name:")
print('hello', y)
