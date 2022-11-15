# JSON is storing and exchanging data 
# JSON is text , writen with javascript object notation 
# Python has built in package called json,which can be work with json data

# Parse json convert from json to python
# if you have a JSON string, you can parse it by using the json.loads() method
# The result will be python dictionary

# Convert from JSON to python 
import json

# Some json
x = '{ "name":"john", "age":36, "city":"new york"}'

# Parse x
y = json.loads(x)

# the result is a python dictionary
print(y["age"])


# Convert from python to json
# if you have a python object, you can convert into a JSON string by using the json.dumps()
# method 
# Convert from python to json

import json
# A python object
x = {
    "name": "john",
    "age": 30,
    "city": "new york"
}

# convert into JSON
y = json.dumps(x)

# The result is json string
print(y)

# we can convert the following python objects into json strings

# dict
# list
# tuple
# string
# int
# float
# string
# Flase
# True
# None

# Convert python object into json strings
print(json.dumps({"name": "john", "age": 30 }))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps('helo'))
print(json.dumps(42))
print(json.dumps(37.89))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

# When you convert from python to json, Python object converted into JSON equivalent


# Python                                                JSON
# dict                                                  Object
# list                                                  Array
# tuple                                                 Array
# str                                                   String
# int                                                   Number
# Flaot                                                 Number
# True                                                  true
# False                                                 false
# None                                                  null


# Convert Python object that contain all legal types
import json
x = {
    "name": "john",
    "age": 36,
    "married": True,
    "divorced": False,
    "children" : ("Ann", "Billy"),
    "Pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

print(json.dumps(x))

# Format the result

# The example above prints the json string but its not very easy to read, with no indentions and line breaks
# The json.dumps() method has parameters to make it easier to made the result 
# use the indent parameter to define the numbers of indents 

t = json.dumps(x, indent=4)
print(t)

# you can also define the separators, default value is (",",":") which means using a commma and a
# space to separete each object, and a colon and a space to separate keys from values
# Use the separators to change the default separator

k = json.dumps(x, indent=4, separators = (".", "="))
print(k)


# Order the result
# Json.dumps parameter method has parameters to order the keys in the result

# Use the sort_keys parameter to specify the result should be sorted or not 

l = json.dumps(x, indent=4, sort_keys=True)
print(l)

