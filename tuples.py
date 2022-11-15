# A tuple is a collection which is ordered and unchangeable allows duplicate members. In python tuples are written with round brackets
# Create tuple
thistuple = ('apple', 'banana', 'cherry')
print(thistuple)

# Access tuple items 
# you can access tuple items by referrring to the index number, inside square brackets
# print the second item in the tuple

thistuple = ('apple', 'banana', 'cherry')
print(thistuple[1])


# negative indexing 
# negative indexing means starting from the end -1, refers to the last item, -2 refers to the second last
# item 
# print the last item of the tuple
thistuple = ('apple', 'banana', 'cherry')
print(thistuple[-1])

# Range of indexes 
# you can specify range of indexes by specifying where to start and where to end range.
# when specifying   a range the return value will be a tuple with the specified items
# Return the third, fourth, fifth items
thistuple = ('apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango')
print(thistuple[3:6])

# range of negative indexes 
# Specify negative indexes if you want to start the search from end of the tuple
# the below example returns the items from -4 to index -1(excluded)
thistuple = ('apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango')
print(thistuple[-4:-1])

# Change tuple values 

# Once the tuple is created, you can not change its values. Tuples are unchangeable, or
# immutable as it also is called

# But there is work around. you can conevert the tuple into list, and convert the list back into a tuple
# convert the tuple into list to be able to change the  values
x = ('apple', 'banana', 'cherry')
y = list(x)
y[1] = 'kiwi'
x = tuple(y)


print(x)

# Loop through a tuple items by using a for loop
# Iterate through the items and print the values 

thistuple = ('apple', 'banana', 'cherry')
for x in thistuple:
    print(x)

# check if item exists
# To determine if a specified item is present in A tuple use in keyword
# check if 'apple' is present in the tuple
thistuple = ('apple', 'banana', 'cherry')
if 'apple' in thistuple:
     print(' Yes, apple is in the fruits tuple')

# To determine how many items a tuple has, use the len() method
# print the number of items in a tuple
thistuple = ('apple', 'banana', 'cherry')
print(len(thistuple))

# Add items 
# Once a tuple is created, you can not add items to it. tuples are unchangeable
# You can not add items to a tuple

'''thistuple = ('apple', 'banana', 'cherry')
thistuple[1] = 'orange' # it will raise the error
print(thistuple)'''

# Create a tuple with one item 
# To create a tuple with one item you have to add a comma after the item, unless python 
# won't recognize the variable as a tuple

# one item tuple remember the comma 
thistuple = ('apple',)
print(type(thistuple))

thistuple = ('apple') # not a tuple
print(type(thistuple))

# Remove items 
# tuples are unchangeable so you can not remove the items from it, but you can delete completely
# The del keyword can delete the tuple completely
thistuple = ('apple', 'banana', 'cherry')
del thistuple
# print(thistuple) # name thistuple is not defined

# join two tuples 
# to join two tuples you can use + operator
tuple1 = ('a', 'b', 'c')
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

# The tuple constrctor
# It is also possible to use tuple() constructor to make a tuple
# using the tuple() method to make the tuple
thistuple = tuple(('apple', 'banana', 'cherry')) # note the double rounded brackets
print(thistuple)

# count()  method
# Returns the number of times a specified value occurs in a tuple

thistuple = (1, 3, 4, 2, 5, 3, 6, 5)
x = thistuple.count(5)
print(x)

# index() method will return only first occurance of specified value

thistuple = ('apple', 'banana', 'cherry')
x = thistuple.index('apple')
print(x)