# Python classes 
# Python is an object oriented programing language
# Almost everything in python is object, with its properties and methods
# A class is like an object constructor, or a blue print for creating objects

# Create a class
# use the keyword class

class MyClass:
    x = 5

# create an object
# now we can use the class named myclass to create objects
# create an object named p1 and print the value of x

p1 = MyClass()
print(p1.x)

# The init function 
# The examples above are classes and objects in their simplest form, and are not really useful in real life
# To uderstand the meaning of classes we have to understand the builtin init function
# all classes have a function called init which is always executed when the class is being initiated
# Use the init function to assign values to object properties or other operations that are neccessary to do
# when the object is being created 
# Create class named person, use the init function to assign values for name and age

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age 
p1 = Person('John', 36)

print(p1.name)
print(p1.age)

# The init function is called automatically every time class is being used to create new object
# object methods 
# objects can also contain methods. Methods in objects are functions that belong to the object
# Let us create the function in Person class
# Insert a person that prints greeting,and execute it in p1 object

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print('Hello my name is ' + self.name)


p1 = Person('John', 36)

p1.myfunc()

# NOte that self parameter is reference to the current instance of the class, and is used to access the 
# variables that belongs to the class

# The self parameter is a reference to the current instance of the class and is used to access the
# variables that belongs to the class

# It does not have to be named self, you can call it whatever you like, but it has to be the 
# first parameter of any function in the class

# use the words mysillyobject and abc instead of self

class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age
    def myfunc(abc):
        print('hello my name is ' + abc.name)
p1 = Person('john', 36)
p1.myfunc()

# Modify object properties on objects like this
p1.age = 25


# delete the object property

del p1.age

# delete objects

del p1
