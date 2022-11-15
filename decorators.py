# decorators 
# Following are important facts about functions in python that are useful to understand decorator
# functions 
# In python we can define a function inside a function 
# In python a function can be passed as parameter to another function

# Adds a welcome message to the string
def messagewithwelcome(str):

    #Nsted function
    def welcome():
        return 'welcome to '

    # Return cancatenation of welcome 
    # and str
    return welcome() + str

# to get site name which welcome is added
def site(site_name):
    return site_name

print(messagewithwelcome('geeksforgeeks'))


# function decorator
# A decorator is a function that takes a function as its only parameter and returns a function.
# this is helpful to wrap functionality with the same code over and over again 
# the above code can be written as follow
# we use @func_name to specify decorator to be applied on another function

# Adds welcoome message to the string
# returned by fun(). takes fun() as 
# parameter and returns welcome()
def decorate_message(fun):

    # nested function
    def addWelcome(site_name):
        return 'welcome to' + fun(site_name)

    # Decorator return the function
    return addWelcome

@decorate_message
def site(site_name):
    return site_name

# Driver code 
# this call is equivalent to call to 
# decorate_message () with function
# site('geeksforgeeks) as parameter
print(site('geeks for geeks'))

# Decorator can also be useful to attach data to functions
# A python example to demonstrate that 
# Decorators can be useful to attach data to functions

# data to func
def attach_data(func):
    func.data = 3
    return func

@attach_data
def add(x, y):
    return x + y

print(add(2, 3))

print(add.data)