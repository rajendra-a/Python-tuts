# Inheritance allows us to define a class that inherites all the properties and methods
# Parent class is class being inherited from, also called base class
# Child class is class that inherits from another class, also called derived class

# Create a parent class 
# any class can be parent class
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    
    def printname(self):
        print(self.firstname, self.lastname)
    

# Use the person class to create an object, and then execite the  printname method
x = Person('john', 'doe')
x.printname()


# Create child class

class Student(Person):
    pass

# Use the pass keyword when you do not want to add  any other properties or methods to class
# Now the student has the same properties and methods as the person class
# use the student class to create object

x = Student('rajendra', 'reddy')
x.printname()


# Add the __init__ function 
# So far we created a child class that inherits the  properties and methods from its parent
# We want to add __init__ funciton to the child class
# The __init__ method called automatically every time the class is being used to create a new object

# Add __init_ function  to the student class
class Student(Person):
    def __init__(self, fname, lname):
        f = fname

# When you add __init__() function, the child class will no longer inherit the parent init
# the childs __init__() function overrides the inheritance of the parents init functionn

class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)
    
# now we have successfully added the __init__() function, and kept the inheritance of the parent class
# and we are ready to add functionality in the init function 

# Use the super() function 
# python also have a super function that will make the child class inherit all the methods and
# properties from its parent 

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019
        
# # add a year parameterm, and pass the correct year when creating objects

# class Student(Person):
#     def __init__(self, fname, lname, year):
#         super(Person, self).__init__(fname, lname)
#         self.graduationyear = year

# x = Student('john', 'doe', 2019)


# Add a method called welcome to the student class


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print('welcome' + self.firstname , self.lastname + 'to the class of '+ self.graduationyear)

# If you add a  method in the child class with same name as a function in the parent class
# the inheritance of the parent method will be overriden 
