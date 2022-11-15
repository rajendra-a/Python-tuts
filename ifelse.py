# python conditions and if statements
# Python supports the usual logical conditions from mathematics 

# if statement
a = 33
b = 200

if b > a:
    print(' b is greater than a')

# Indentation 
# python relies on indentation to define scope in the code
# other programing languages uses curly brace for the purpose

# the elif keyword is pythons way of saying 'if the previous conditoins were not true,
# then try this condition 
a = 33
b = 33
if b > a:
    print('b is greater than a')
elif a == b: 
    print(' a is equal to b')

# the else statement catches anything which isn't caught by the preceeding conditions
a = 200
b = 33
if b > a:
    print( 'b is greater than a')
elif a == b:
    print('a and b are eqaul')
else:
    print('a is greater than b')


# Shorthand if 
# if you have only one statement to execute, you can put it on the same line as the if statement
# one line if statement
if a > b: print('a is greater than b')

# shorthand if else
a = 2
b = 330
# print('A') if a > b else print('B') #  getting invalid syntax while runnig 

# one line if else statement, with 3 conditions
a = 330
b = 330
# print('A') if a > b else print('=') if a == b else print('B') 

# And keyword is a logical operator and is used to combine conditional statements
# Test if a greater than b, AND if c is greater than a
a = 200
b = 33
c = 500
if a > b and c > a: 
    print('Both conditions are true')

# the or keyword is a logical operator and is used to combine conditional statements
a = 200
b = 33
c = 500

if a > b or a > c:
    print('At least one of the conditions is True')

# Nested if
# You can have if statements inside if statements this  is called nested if statements

x = 41
if x > 10:
    print('Above ten,')
    if x > 20:
        print('and, also above 20')
    else:
        print('but not above 20')
