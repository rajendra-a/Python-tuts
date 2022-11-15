# A dictionary is a collection which is unordered, changeable and indexed, in python dictionaries written in curly brackets
# and they have keys and values
thisdict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1946
}

print(thisdict)

# you can access the items of a dictionary by referring to its key name, inside square brackets
# Get the value of model key

x = thisdict['model']
print(x)

# there is also method called get that will give you the same result
# Get the value of model key
x = thisdict.get('model')
print(x)

# you can change the value of a specific item by refrring to its key name
# change the year
thisdict['year'] = 2019
print(thisdict)

# you can loop through a dictionary using a for loop
# when looping through a dictionary the return values are keys of the dictionary
# but there are methods to return values of the keys

for x in thisdict:
    print(x) # return all keys 

# print all values in the dictionary one by one
for x in thisdict:
    print(thisdict[x])

# you can also use values function to return values
for x in thisdict.values():
    print(x)

# loop through both keys and  values by using items function
for x, y in thisdict.items():
    print(x, y)
# check if key exists
# To determine if a specified key present in a dictionary use the in keyword

# check if the model present in the dictionary or not 
thisdict = {
    'brand': 'ford',
    'model': 'year',
    'year': 1946
}

if 'model' in thisdict:
    print('yes, model is the one of the keys in thisdict dictionary')

# Dictionary length
# To determine how many items a dictionary has, use the len() method
# print the number of items in a dictionary
print(len(thisdict))

# Adding items to the dictionary is done by using a new key index by assigning a value to it
thisdict = {
    'brand': 'ford', 
    'model': 'mustang',
    'year': 1946
}

thisdict['color'] = 'red'

# Removing items from a dictionary
# there are several methods to remove items from a dictionary 
# the pop() method will remove the item with the specified key name
thisdict = {
    'brand': 'ford',
    'model': 'Mustang',
    'year': 1946
}

# The pop method removes the item with the specified key name

thisdict = {
    'brand': 'ford',
    'model': 'mustang',
    'year': 1946
}

thisdict.pop('model')

print(thisdict)


# The popitem() method removes the last inserted item(in versions before 3.7, a random item is removed instead)
thisdict = {
    'brand': 'Ford',
    'model': 'mustang',
    'year': 1946
}

thisdict.popitem()
print(thisdict)

# The del keyword removes the item with the specified keyname
thisdict  = {
    'brand': 'ford',
    'model': 'mustang',
    'year': 1946
}

del thisdict['model']

print(thisdict)

# The del keyword also delete the dictionary completely
thisdict = {
    'brand': 'ford',
    'model': 'mustang',
    'year': 1946
}

del thisdict
# print(thisdict) # raise error because thisdict is no longer exists

# The clear() method empties the dictionary
thisdict = {
    'brand': 'ford',
    'model': 'mustang',
    'year': 1946
}

thisdict.clear()
print(thisdict)

# Copy the dictionary
# you cannot copy a dictionary simply by typing dict2 = dict1, becuase dict2 only be reference to 
# dict1, and changes made in dict1 will automatically also made in dict2 
# there are ways to make copy, one way is use the built in dictionary method copy()
# Make a copy of a dictionary with copy() method

thisdict = {
    'brand': 'ford',
    'model': 'mustang',
    'year': 1947
}

mydict = thisdict.copy()
print(mydict)

# another way to make a copy is to use built in dict() method
thisdict = {
    'brand': 'ford',
    'model': 'mustang',
    'year': 1946
}

mydict = dict(thisdict)
print(mydict)


# Nested dictionary
# a dictionary can also contain many dictionaries
# this is called nested dictionaries

myfamily = {
    'child1': {
        'name': 'Emil',
        'year': 2004
    },
    'child2': {
        'name': 'tobias',
        'year': 2007
    },
    'child3': {
        'name': 'linus',
        'year': 2011
    }
}

# Or if you want to nest three dictionaries that already exists as dictionaries
child1 = {
    'name': 'emil',
    'year': 2004
}

child2 = {
    'name': 'tobias',
    'year': 2007
}

child3 = {
    'name': 'linus',
    'year': 2011
}

myfamily = {
    'child1': child1,
    'child2': child2,
    'child3': child3
}

print(myfamily)

# The dict constructor
# It is also possible to make a dict constructor

thisdict = dict(brand='ford', model='mustang', year=1946)
# note that keywords are not string literals
# note that use of equal rather than colon for assignment


# fromkeys()
# the fromkeys() return a dictionary with the specified keys and values
x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict)

x = ('key1', 'key2', 'key3')
thisdict = dict.fromkeys(x)

print(thisdict)

# Python dictionary keys() method 
# the keys() method returns a view object that object . this view object contains the keys of the dictionary
# as a list The view object will reflect any changes done to the dictionary 
car = {
    'brand': 'ford',
    'model': 'mustang',
    'year': 1946
}

x = car.keys()
car['color'] = 'white'
print(x)

# The setdefault() method returns the value of the item with the specified key 
# If the key does not exist, insert the key, with the specified value 

car = {
    'brand': 'ford',
    'model': 'mustang',
    'year': 1946

}

x = car.setdefault('model', 'bronco')

print(x)

#update()
# the update method inserts the specified items to the dictionary
# the specified items can be a dictionary or an iterable object

car = {
    'brand': 'ford',
    'model': 'mustang',
    'year': 1946
}

car.update({'color': 'white'})