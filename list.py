# List is a collection which is ordered and changeable allows dupllicate members. In python lists are written with square brackets
# Create list 
thislist = ['apple', 'banana', 'cherry']
print(thislist)

# Access items by referring the index number
# print the second item of the list
thislist = ['apple', 'banana', 'cherry']
print(thislist[1]) 

# Negative indexing
# negative indexing means begining from the end, -1 refers to the last item, -2 refers to the second last item etc.
# print last item from the list
thislist = ['apple', 'banana', 'cherry']
print(thislist[-1])

# Range of indexes 
# you can specify range of indexes by specifying where to start and where to end the range.
# When specifying a range, the return value will be newlist with the specified items 

# Return the third fourth and fifth item 
thislist = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
print(thislist[2:5])

# Note the search will start at index 2(included) and end at index 5 (not included)
# Remember the first item has index 0

# Range of negative indexes
# specify negative indexes if you want to start the search from the end of the list
thislist = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
print(thislist[-4:-1])

# Change the item value
# To change the value of specified item, refer to the index number
# change the second item 
thislist = ['apple', 'banana', 'cherry']
thislist[1] = 'blackcurrant'
print(thislist)

# Loop thorough a list
# you can loop thorough the list items by using for loop
# print all items in list one by one
thislist = ['apple', 'banana', 'cherry']

for x in thislist:
    print(x)

# Check if item exists 
# To determine if a specified item is present in a list use in keyword

# Check if apple present in the list
thislist = ['apple', 'banana', 'cherry']

if 'apple' in thislist:
    print('yes, apple in the fruits list')

# List length 
# To determine how many items a list has, use the len method
thislist = ['apple', 'banana', 'cherry']
print(len(thislist))

# Add items 
# To add an item to the end of the list, use append method
# Using append method to append an item

thislist = ['apple', 'banana', 'cherry']
thislist.append('orange')
print(thislist)


# To add an item to the specified index, use the insert method
# Insert an item as the second item

thislist = ['apple', 'banana', 'cherry']
thislist.insert(1, 'orange')
print(thislist)

# remove item 
# There are several methods to remove items from a list
# the remove method removes specified item
thislist = ['apple', 'banana', 'cherry']
thislist.remove('banana')
print(thislist)

# The pop() method removes specified index, (or the last item if the index is not specified)
thislist = ['apple', 'banana', 'cherry']
thislist.pop()
print(thislist)

# the del keyword removes the specified index

thislist = ['apple', 'banana', 'cherry']
del thislist[1]
print(thislist)


# The del keyword also removes list completely
del thislist

# Clear() method empties the list

thislist = ['apple', 'banana', 'cherry']

# thislist.clear()

print(thislist)


# Copy a list
# you can not copy the list by simply typing list2 = list1, because: list2 will only be a reference to list1,
# and changes made in list1 will automatically also be made in list2
# there are ways to make a copy, one is to use the built in list method copy()

# Make a copy of the list with the copy method

thislist = ['apple', 'banana', 'cherry']
# mylist = thislist.copy()
# print(mylist) 

# Another way to make a copy is to use the built in method list()
# Use the extend() method, which purpose is to add elements from one list to another list
# Make a copy of the list with list() method

thislist = ['apple', 'banana', 'cherry']
mylist = list(thislist)
print(mylist)

# Join Two lists 
# there are several ways to join, or concatenate, two or more lists in python 
# one of the easiest ways are by using the + operator

# Join Two list
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# Another way to join two lists are by appending all the items from list2 into list1, one by one
# Append list2 into list1
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)
print(list1)

# Or you can use the extend() method, which purpose is to add elements from onelist to another list
# Use the extend() method to add list2 at the end of list1:
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

# the list() constructor
# It is also possible to use the list() constructor to make a newlist
# Using the list constructor to make a list

thislist = list(('apple', 'banana', 'cherry'))
print(thislist)


# Python List count() method 
# Return the number of times the value occured in list 
fruits = ['apple', 'banana', 'cherry']
x = fruits.count('apple')
print(x)


#Index() method
# Returns the position at the first occurence of the specified value
numbers = [1, 2, 4, 25, 45, 4, 6, 7, 4]
x = numbers.index(4)
print(x) 


# Reverse()
# reverse the order of fruit list
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)


# sort()
numbers = [1, 7, 9, 4, 5, 6]
numbers.sort()
print(numbers)

# To sort in reverse order
numbers.sort(reverse=True)
print(numbers)

# list comprehensions
h_letters = [letter for letter in 'human']
print(h_letters)

number_list = [ x for x in range(20) if x %2 ==0]
print(number_list)

num_list = [x for x in range(100) if x % 2 == 0 and x % 5 ==0]
print(num_list)


evens = ["Even" if x%2 == 0 else "odd" for i in range(10) ]
print(evens)

# Transpose of a matrix using list comprehensions
matrix = [[1, 2], [3, 4], [5, 6]]
transpose = [[row[i] for row in matrix]for i in range(2)]
print(transpose)

