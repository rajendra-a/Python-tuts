
# Python sets
# A set is a collection which is unordered and unindexed. In python sets are written in curly braces
# create a set
thisset = {1, 2, 3, 4, 5}
print(thisset)
# Sets are unordered, so you can not be sure in which order items will appear

# Access items 
# you can not access items in a set by an index, since sets are unordered
# the items have no index
# but you can loop through set items using for loop, or ask if a specified value present in a set \
# by using the in keyword

# Loop through the set items and print values
thisset = {'apple', 'banana', 'cherry'}
for x in thisset:
    print(x)

# check if banana present in set
thisset = {'apple', 'banana', 'cherry'}
print('banana' in thisset)

# Once set is created you can not change items, but you can add new items
# Add items
# To add one item to set use add() method 
# To add  more than one item to a set use update() method

# Add an item to a set, using add method
thisset = {'apple', 'banana', 'cherry'}
thisset.add('orange')
print(thisset)

# Add multiple items to a set
thisset = {'apple', 'banana', 'cherry'}
thisset.update(['orange', 'kiwi', 'mango'])
print(thisset)

# Get the lenght of the set
thisset = {'apple', 'banana', 'cherrry'}
print(len(thisset))

# Remove an item
thisset = {'apple', 'banana', 'cherry'}
thisset.remove('banana') # If the item not found remove method raise exception
print(thisset)

# remove banana by usig discard method
thisset = {'apple', 'banana', 'cherry'}
thisset.discard('banana') # if the item to remove does not exist discard method will not raise error
print(thisset)

# You can also use pop method to remove item but this method will remove last item
thisset = {'apple', 'banana', 'cherry'}
x = thisset.pop()
print(x)
# sets are unordered, so when using pop() method, you will not know which item that gets removed
# the return value of pop method() is the removed item

# clear method() empties the set
thisset = {'apple', 'banana', 'cherry'}
thisset.clear()
print(thisset)

# del keyword delete the set completely
thisset = {'apple', 'banana', 'cherry'}
del thisset
# print(thisset) # raise an error as name thisset can not defined

# Join two sets there are several ways to join two or more sets 
# you can use the union method that returns a new set containing all items from both sets,
# or the update() method that inserts all items from both sets 

set1 = {1, 2, 3, 4}
set2 = {'a', 'b', 'c', 1}

set3 = set1.union(set2)
print(set3)

set4 = set1.update(set2)
print(set4)

# Both union and update methods will exclude any duplicate items
# There are other methods to that joins two sets and keeps only the duplicates, or never the duplicates

# set() contructor
# It is also possible to use set constructor to make a set

thisset = set(('apple', 'banana', 'cherry'))

# Copy()
fruits = {'apple', 'banana', 'cherry'}
x = fruits.copy()
print(x)

# The difference method returns a set that contains the difference between two sets
# the returned set contains items that exist only in the first set and not in the both sets
x = {'apple', 'banana', 'cherry'}
y = {'gogle', 'microsoft', 'apple'}
z = y.difference(x)
print(z)


# differnce update
# The difference_update method removes the items that exist in both sets
# The difference_update method is different from difference() method because difference method returns new 
# set, without the unwanted items, and the difference update method removes the unwanted items from the original set

x = {'apple', 'banana', 'cherry'}
y = {'google', 'microsoft', 'apple'}
x.difference_update(y)
print(x)


# Intersection()
# Returns a set that contains the similarity between two or more sets
# Meaining: the returned set contains only items that exists in both sets, or in all sets
# if the comparision done with more than two sets

x = {'apple', 'banana', 'cherry'}
y = {'google', 'microsoft', 'apple'}

z = x.intersection(y)
print(z)

# compare three sets, and return a set with items that is present in all 3 sets
x = {'a', 'b', 'c'}
y = {'c', 'd', 'e'}
z = {'f', 'g', 'c'}

result = x.intersection(y, z)
print(result)

# the intersection_update() method removes the items that is not present in both sets 
# the intersection_update() method is different from the intersection method, because the intersection method
# returns a new set, without the unwanted items, and the intersection_update() method removes the 
# unwanted items from original set
x = {'apple', 'banana', 'cherry'}
y = {'google', 'microsoft', 'apple'}

x.intersection_update(y)
print(x)

# isdisjoint() method returns True if none of the items are present in both sets, otherwise it returns false
x = {'apple', 'banana', 'cherry'}
y = {'google', 'microsoft', 'apple'}
z = x.isdisjoint(y)
print(z)

# issubset() method returns the True if all items in the set exists in the specified set, otherwise it returns false
x = {'a', 'b', 'c'}
y = {'f', 'e', 'd', 'c', 'b', 'a'}
z = x.issubset(y)
print(z)

# issuperset method returns True if all items present in the specified set that exist in original set 
# Otherwise it returns false
x = {'f', 'e', 'd', 'c', 'b', 'a'}
y = {'a', 'b', 'c'}

z = x.issuperset(y)
print(z)

# the symmetric_difference method 
# symmetric_differece method returns a set that contains all items from both sets, but not the items
# that are present in the both sets  
x = {'apple', 'banana', 'cherry'}
y = {'google', 'microsoft', 'apple'}
z = x.symmetric_difference(y)

# the symmetric_difference_update()
# this method return updated set by removing items that are present in both sets, and inserting the other items

x = {'apple', 'banana', 'cherry'}
y = {'google', 'microsoft', 'apple'}
x.symmetric_difference_update(y)
print(x)