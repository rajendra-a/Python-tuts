# Python Loops
# Python has two primitive loops 
# while loops 
# For loops


# The while loop we can execute a set statements as long as condition is true
# print i as long as i less than 6

i = 1
while  i < 6:
    print(i)
    i += 1 

# remember to  increament i, or else the loop will continue forever

# The while loop requires relavant variable to be ready, in this example we need to define
# an indexing variable i,, which is set to 1

# the break statement
# with the break statement we can stop the loop even if the while condition is true

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# Continue statement 
# with the continue we can stop the current iteration and continue with the next

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

# else statement we can run a block of code when the conditin is no longer is True
# Continue to the next iteration if i = 3

i = 1
while i < 6:
    print(i)
    i += 1
else:
    print('i is no longer less than 6')