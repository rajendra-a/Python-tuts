# A for loop is used for iterating over sequence
# this is less like the for keyword in other programing languages, and works more like an iterator 
# method as found in other object oriented programing languages
# with the for loop we can execute a set of statements,once for each item in a list, tuple etc.

fruits = ['apple', 'banana', 'orange']
for x in fruits:
    print(x)

# The for loop does not require an indexing variable to set beforehand
# Looping through a string
# Even strings are iterable objects, they contain a sequence of characters

for x in 'banana':
    print(x)

# With break statement we can stop the loop before it has looped through all the items
# exit the loop when x is banana

fruits = ['apple', 'banana', 'cherry']
for x in fruits:
    print(x)
    if x == 'banana':
        break

# With the continue we can stop the current iteration of the loop, and continue with the next 
# do not print banana

fruits = ['apple', 'banana', 'cherry']
for x in fruits:
    if x == 'banana':
        continue
    print(x)


# The Range() function
# TO through a set of code a specified number of times, we can use the range() function
# the range function returns a sequence of numbers starting from 0 by default and increaments by 1
# ends at a specified number

for x in range(6):
    print(x)

# note that range(6) is not the values of 0 to 6 but 0 to 5
# The range function defaults to 0 as a starting value, however it is possible to specify 
# the starting value by adding a parameter:range(2, 6) 
for x in range(2, 6):
    print(x)

# the range() function default to increament the sequence by 1, however it is possible to specify
# the increament value by adding this parameter range(2, 30, 3)
# increament sequence with 3
for x in range(2, 30, 3):
    print(x)

# Else in for loop
# the else keyoword in a for specifies a block of code that execute after for loop is finished
for x in range(6):
    print(x)
else:
    print('finally finished')

adj = ['red', 'big', 'tasty']
fruits = ['apple', 'banana', 'cherry']

for x in adj:
    for y in fruits:
        print(x, y)