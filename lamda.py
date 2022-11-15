# Python Lambda
# A Lambda function is small anonymous function 
# A Lambda can take any number of arguments, but can only have one expression
# The expression is executed and the result is returned

x = lambda a: a + 10  
print(x(5))

x = lambda a ,b: a * b 
print(x(5, 6))

x = lambda a, b, c: a + b + c
print(x(2, 3, 4))

# Why use lamda functions
# the power of lambda is better shown when you use them as an anonymous function inside another function
# Say you have function definition that takes one argument and that argument will be multiplied with
# an unknown number

def myfunc(n):
    return lambda a: a * n

# Use that function definition to make a function tha always doubles the number that you send in 

def my_func(n):
    return lambda a: a * n

mydoubler = my_func(2) 
print(mydoubler(11))

# Or use the same function definition to make a function that always triples the number you send in

def my_fun(n):
    return lambda a: a * n

mytripler = my_fun(3)
print(mytripler(11))

# Use lambda functions when anonymous function is required for a short period of time


# Python does not have support for arrays, but python lists can be used instead 
# Arrays are used to store multiple values in single varialbe
# Create an array containing car names 

cars = ['Ford', 'Volvo', 'BMW']

# What is an array
# An array is special variable which holds more than one item at a time 
# If you have a list of items, storing the cars in single variable looks like this 
car1 = 'Ford'
car2 = 'Volvo'
car3 = 'BMW'