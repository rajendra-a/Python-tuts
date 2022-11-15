# Boolean represents one of two values: true or false
# Boolean values
# In programing you often need to know if an expression is True or False
# You can evaluate any expression in Python, and get one of two answers, True or False
# When you compare two values, the expression is evalueated an Python returns the Boolean answer
print(10 > 9)
print(10 == 9)
print(10 < 9)

# When you run a condition in an if statement Python returns true or false

# Print a message based on weather the condition is True or False
a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# Evalueate values and variables
# The bool function allows you to evaluate any value, and give you true or false in retrun

# Evaluate a string and a number
print(bool("Hello"))
print(bool(2))

# Most values are True
# Almost any value evaluated to true if it has some sort of content
# Any string is true except empty string 
# Any number is true except 0
# Any list, tuple, set and dictionary are true, except empty ones

# The following will return true
bool('abc')
bool(123)
bool(['apple', 'cherry', 'banana'])

# Some values are false
# In fact there are not many values that evaluates to false, except empty values, such as (), [], {},""
# the number 0, and the value none. and of course the value false evaluates to false
# The following return false
bool(False)
bool(None)
bool("")
bool(0)
bool([])
bool(())
bool({})

# One more value, or object in this case, evaluates to false, and that is if you have an object that are made from
# a class with a _len_ function that returns 0 or false
class myclass():
    def __len__(self):
        return 0
myobject = myclass()
print(bool(myobject))

# Functions can return a boolean 
# python also has many built-in functions that returns a boolean value, like the isinstance() function,
# which can be used to determine if an object is of a certain data type:
x = 200
print(isinst(x, int))