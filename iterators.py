# Iterators 
# Iterator is an object that contains countable number of values 
# An iterator is an object that can be iterated upon, meaning that you can traverse through 
# all the values
# Technically in python iterator is an object which implements iterator protocal, which consists
# of methods __iter__() and __next__()

# Iterator vs iterable
# Lists , tuple , dictionary and sets are iterable objects. They are iterable containers, which you can get iterator from
# All these objects have a  iter() method which is used to get an iterator 
mytuple = ('apple', 'banana', 'cherry')
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

# Even strings also iterable objects, containing a sequence of characters
mystr = 'banana'
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

# Looping through an iterator
# We can also use a for loop to iterate through an iterable object
mytuple = ('apple', 'banana', 'cherry')
for x in mytuple:
    print(x)

# Iterate the charecters of string 

mystr = 'banana'
for z in mystr:
    print(z)

# The for loop actually creates an iterator object and executes the next() method for each loop
# Create an iterator 
# To create an itarator you have to implement the methods __iter__() and __next__()
# to your object
# As you learned in python classes/objects chapter, all classes have a function called __init__()
# which allows you do some initializing when the object is being created 
# the iter() method acts similar, you can do operations, but must alwyas return the iterator object itself

#Create an iterator that returns numbers, starting with 1,and each sequenc increase by 1

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

# Stop iteration 
# The example above continue forever if you had enough next() statements or if it was used in a
# for loop to prevent the iteration to go on forever, we can use the stop iteration statement
# In the next() method, we can add a terminating condition to raise an error if the iteration done
# a specified number of times

class MyNumber:

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 9:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass1 = MyNumber()
myiter1 = iter(myclass1)
# print(next(myiter1))
# print(next(myiter1))
# print(next(myiter1))
# print(next(myiter1))
# print(next(myiter1))
# print(next(myiter1))
# print(next(myiter1))
# print(next(myiter1))

