# Python functions
# A function is a block of code which only runs when it is called
# you can pass data, known as parameters, into a function
# A function can return data as a result
# In python a function is defined using def keyword

def my_fuction():
    print('hello from a function')

# To call a function, use the function name followed by paranthesis

def my_function():
    print('hello from a function')

# Patameters 
# Information can be passed to functions as parameters 
# Parameters specified after the function name inside the paranthesis. you can add as many parameters
# as you want, just separate them with a commma
# The following example has a function with one parameter, when the function is called, we
# pass along a first name which is used inside the function to print the full name

def my_function(fname):
    print(fname + ' refsnes') 

my_function('Emil')
my_function('Tobias')
my_function('Linus')


# Default parameter value
# The following example shows how to use default parameter value 
# If we call the parameter without parameter, It uses the default value

def my_function(country='norway'):
    print('I am from ' + country)

my_function()
my_function('India')
my_function('brazil')

# passing list as a parameter
# You can send any type of parameter to a function and it will be treated as the same data type inside the function
# If you send list as a parameter, It will still be a list when it reaches the function

def my_function(food):
    for x in food:
        print(x)

fruits = ['apple', 'banana', 'cherry']
my_function(fruits)

# Return value 
# To let a funciton return a value, use the return statement

def my_function(x):
    return x * 5

my_function(3)
my_function(5)
my_function(9)

# Keyword arguments
# you can also send the arguments with the key = value syntax
# this way the order of the arguments does not matter
def my_function(child3, child2, child1):
    print('The youngest child is ' + child3)

my_function(child1 = 'Emil' , child2 = 'Tobias', child3 = 'Linus')

# The phrase Keyword arguments are often shortened to kwargs in python documentations

# Arbitary arguments
# If you do not know how many arguments that will be passed into your function, add a * before
# the parameter name in the functoin definition 
# this way function receives the tuple of arguments, and can access the items accordingly

def my_function(*kids):
    print('The youngest kid is ' + kids[2])

my_function('Emil', 'Tobias', 'Linus')

# Python also accepts the function recursion, which means a defined function can call itself
# This has the benefit of the meaning that you can loop through data to reach a result
# The developer should be very careful with recursion as it can be quite easy slip into writig function
# which never terminates, or one that uses excess amount of memory or processor power
# In this example try_recursion is a function that we can defined to call itself we use k variable as data
# which decreaments everytime we recurse. the recursion ends with when the condition is not greater than 0

def try_recursion(k):
    if k > 0:
        result = k + try_recursion(k-1)
        print(result)
    else:
        result = 0
    return result
try_recursion(6)
