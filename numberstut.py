# Numbers
# There are three  numeric types in Python:
# Int
# Float
# complex
# Variables of numeric types are created when you assign a value to them
x = 1 # Int
y = 2.8 # Float
z = 3j  # Complex

# To verify the type of an object use type function
print(type(x))
print(type(y))
print(type(z)) 

# Float can also be scientific numbers with an "e" to indicate the  of 10
x = 35e5

# Type conversion
# you can convert one type to another with the int(), float(), complex methods

x = 1 
y = 2.8
z = 1j

# convert from int to float
a = float(x)
b = int(y)
c = complex(x)

print(a)
print(b)
print(c)

# Note you can not convert complex numbers to another number type


# Random number 
# Python doesn't have a random() function to make a random number, but python has built in module 
# called random that can be used to make random numbers
# Example
# import random module and print a number between 1 to 9 
import random

x = random.randrange(1, 10)
print(x)

y = random.choice(seq)