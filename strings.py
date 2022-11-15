# String literals in python are surrounded by either single quotation marks, or double quotation marks 
# "hello" is same as 'hello'
# You can display the string literal using print() function
print("Hello")
print('Hello')

# You can assign a multiline string to a variable by using three quotes
# You can use three double quotes 
a = """ Rajendra is a good boy,
        he is so ambisious and wise,
        he will do what he wants."""

# or three single quotes
a = ''' Rajendra is a good boy
        he is so ambisious and wise,
        he will do what he wants.'''
print(a)

# In the result the line breaks are inserted at the same position as in the code

# Strings are arrays
# Like many other programing languages, strings in python are arrays of bytes representing unicode characters
# However python does not have a character data type, a single character simply a string with a lenght of 1.
# square brackets can be used to access elements of the string

# Get the character at the position 1
x = "Hello, World!"
print(x[1])

message = 'Hello World'
print(message)

# count the number of characters in a string
print(len(message))

print(message[6:])
print(message[:5])

# count() method returns the number of times a specified value appears in the string
print(message.count('Hello'))
print(message.count('l'))

# find method used to get the starting character in a string
print(message.find('Hello'))
print(message.find('l'))
print(message.find('universe')) # it con't find that so it returns -1 

# replace() method replaces a specified phrase with another specifed phrase
new_message = message.replace('world', 'Universe')
print(new_message)

# String concating
message = 'hello' + ', ' + 'Michael' + '. welcome'
print(message) # this is little bit complicated but for now 
# It is okay but if it is a large then you feel it like complicated track all the variables and 
# symbols

greeting = 'Hello'
name = 'Michael'
message = '{}, {}. welcome'.format(greeting, name)
print(message)

# if you are using python 3.6 or above versions you can use f string

#message = f'{greeting}, {name}. Welcome'
print(message)

# string formatting
person = {'name': 'Rajendra', 'age': 26}
message = 'My name is {} and i am {} years old.'.format(person['name'], person['age'])
print(message)

message = 'iam {1} years old and my name is  {0}'.format(person['name'], person['age'])
print(message)

message = 'My name is {0[name]} and iam {0[age]} years old'.format(person, person)
print(message)
print('rajendra is a good boy')

# Unlike other programing languages python has no command for declaring variables 
# The variable is created the moment you first assign a value to it 
# example 
# variable do not need to be declared with any perticular type and can even change type after they have been set
x = 4 
x = 'new string'

# a variable can have a short name or a descriptive name for python
# rules for python variables 
# A variable name must start with a letter or a underscore character
# A variable cannot start with a number 
# A variable only contains only alphanumeric characters and underscores
# Python allows you to assign values to multiple variables in one line
a , b, c = 'raj', 'anji', 'srinu'
# and you can assign a value for multiple variables
d = e = f = 'Orange'
print(a)
print(b)
print(c)
print(d)
print(e)

for x in range(1, 11):
    print('{:2d} {:3d} {:4d}'.format(x, x*x, x*x*x))

    





# string literals
# String literals in python surrounded by a single quotation marks or double quotation marks
# 'hello' same as "hello"
# you can display a string literal with the print function
print('Hello')
print('hell0')


# Assign a string to a variable is done with variable name followed by an equal sign and the string
a = 'hello'
print(a)

# Multiline string
a = '''rajendra is a good boy,
he is so ambicious and wise
'''

print(a)

# note: in the result, the line breaks are inserted at the same position as in the code
# Strings are arrays
# Like many other programing languages, strings in Python are arrays of bytes representing unicode
# characters However python does not have a character datatype, a single character is simply a string with a length of 1
# Square brackets can be used to access elements of the string.

# Get the character at position 1
a = 'hello, world!'
print(a[1])

# Slicing
# you can return a range of characters by using the slice syntax
# specifying the start index and end index, separeated by a colon, to return a part of the string

# Get the characters from position 2 to position 5(not included)
b = 'hello, world!'
print(a[2:5])

# negative indexing
# Use the negative index to start slice from the end of the string
# Get the characters from 5 to position 1, starting from end of the string:
b = 'hello, world!'
print(b[-5:-2])

# string length
# To get the length of the string, use the len() function
# The len function returns the length of the string
a = 'hello,, world!'
print(len(a))


# String methods
# Python has a set of built in methods that you can use on strings
# The strip method removes any leading and trailing characters(space is the default leading character to remove)
a = ' hello, world! '
print(a.strip())
 
# The lower() method returns the string where all characters are lower case
# Symbols and numbers are ignored 
a = 'Hello, World!'
print(a.lower())

# The upper() method returns the string in the upper case  where all the numbers and symbols are ignored
a = 'hello, world!'
print(a.upper())

# replace method replaces a string with another string
a = 'Hello, World'
print(a.replace('H', 'J'))

# Split method splits the string into list, you can specify the separator
# default separator is the white space
# When the maxsplit is specified, the list will contain specified number of elements plus one

a = 'Hello, World!'
print(a.split(','))

# The casefold() method returns a string where all the characters are lower case 
# This method is similar to the lower() method, but the casefold() method is stronger, more aggressive
# meaning that it will convert more characters into lowercase, and will find more matches when comparing two
# strings and both converted using the casefold method
a = 'HELLO WORLD'
#y = a.casefold()
#print(y)

# capitalize() method
#  The capitalize() method returns a string wherre the first character to uppercase
a = 'hello, world!'
x = a.capitalize()
print(x)

# See what happens if the first character is a number
txt = "26 is my age"
x = txt.capitalize()
print(x)

# encode() method encode the string, using specified encoding. if no encoding is specified
# UTF-8 will be used
name = 'My name is rajendra'
print(name.encode(encoding='ascii', errors='backslashreplace'))
print(name.encode(encoding='ascii', errors='ignore'))
print(name.encode(encoding='ascii', errors='namereplace'))
print(name.encode(encoding='ascii', errors='strict'))
print(name.encode(encoding='ascii', errors='replace'))
print(name.encode(encoding='ascii', errors='xmlcharrefreplace'))

# center()
# center method will center the string using a specified character(optional)
name = 'rajendra'
modified_name = name.center(10, '*')
print(modified_name)

# endswith() method returns true if the string endswith specified value, otherwise false
name = 'rajendra'
print(name.endswith('r'))

# expandtabs()  Sets the tabsize to the specified number of white spaces    
name = 'rajendra'
txt ='H\te\tl\tl\to'
print(txt.expandtabs())
print(txt)
print(txt.expandtabs(2))
print(txt.expandtabs(4))

#join() 
# join memthod takes all the items in an iterable and joins them into one string
# A string must be specidied as separator

mytuple = ['john', 'peter', 'vicky']
x = '#'.join(mytuple)
print(x)

mydict = {'name': 'john', 'country': 'norway'}
separator = '$'
x = separator.join(mydict)
print(x)

# maketrans()
# maketrans method returns traslation talbe to be used in translations
# find()
# find method finds the first occurence of the specified value
# find method returns the -1 if the value is not found
# The find method is almost the same as the index method, the only difference is that index()
# raises the exception if the value is not found

x = 'hello, welcome to my world'
y = x.find('welcome')
v = x.find('helo')
print(y)
print(v)

# Index method finds the first occurence of the specified value 
# The index method raises an exception if the value is not found
# The index method is almost the same as the find method, the only difference is that the
# find method returns -1 if the value is not found but index() method raises an exception 
z = 'hello world'
w = z.index('hello')
print(w)

# isalnum() method returns true if all the characters are alphanumeric, meaning alphabet letter
# and numbers 0-9
txt = 'company12'
x = txt.isalnum()
print(x)

# isalpha() returns true if all the characters are alphabet letters(a-z)
txt = "ComapnyX"
x = txt.isalpha()
print(x)

# isdecimal() method returns True if all the characters are decimals
# This method is used on unicode objects
a = "\u0030"
print(a.isdecimal())

# isdigit() method returns true if all the characters are digits, otherwise false
# Exponets like, are also considered to be digit
a = "\u0030"
b = "\u00B2"

print(a.isdigit())
print(b.isdigit())

# isidentifier()  returns true if the string is a valid identifier, otherwise false
# A string is consider a valid identifier if it only contains alphanumeric letters, or underscore
# A valid identifier cannot start with a number or contain any spaces
a = "MyFolder"
b = "Demo002"

print(a.isidentifier())
print(b.isidentifier())

# islower() method returns True if all the characters are  in lower case, otherwise false
# Numbers, symbols and spaces are not checked, only alphabet characters
a = "hello, world!"
b = "hello 123"
print(a.islower())
print(b.islower())

# isnumeric() method returns true if all the characters are numeric 0-9, otherwise false
# Exponents like 2 3/4 are also considered to be numeric values 
a = "\u0030"
b = "\u00B2"
c = "10km2"

print(a.isnumeric())
print(b.isnumeric())
print(c.isnumeric())

# The isprintable() method returns true if all the characters are printable, otherwise false
# Example of none printable characters can be carriage return and line feed
txt = "Hello!\nAre you #1?"
x = txt.isprintable()
print(x)

# isspace() method returns true if all the characters in a string are white spaces, otherwise false
txt = " s "
x = txt.isspace()
print()

# istitle() method returns True if all words in a text start with upper case letter,
# and the rest of the word are lower case letters, otherwise flase
# Symbols and numbers are ignored
a = "Hello"
b = "HELLO"
c = "22 Names"

print(a.istitle())
print(b.istitle())
print(x.istitle())

# isupper() method returns true if all the characters are in upper case, otherwise false
# numbers, symbols and spaces are not checked, only alphabet characters
a = "Hello World!"
b = "hell0 123"
c = "MY NAME IS RAJENDRA"

print(a.isupper())
print(b.isupper())
print(c.isupper())

# 



# The partition method searches for specified string, and splits the string into a tuple containing three elements
# the first part before the specified string
# the second element contains specified strig
# the third element contains the part after the specified part
# this method search for the first occurence of the specified string

txt = 'i could eat bananas all the day'
x = txt.partition('bananas')
print(x)

# splitlines()
# splitlines method splits a split into a list. The splitting is done at line breaks
txt = 'thank you for the music\n Welcome to the jungle'
x= txt.splitlines(True)
print(x)

txt ='thank you for the music\n Welcome to the jungle'
y = txt.splitlines()
print(y)

# startswith() method returns true if the string startswith the specified value, otherwise false
txt = "hello, welcome to my world"
x = txt.startswith("wel", 7, 20)
print(x)

# Swapcase()
# swapcase() method returns a string where all the upper case letters are  lower case and vice versa
a = "Hello"
print(a.swapcase())


# zfill
# the zfill method()  adds zeros(0) at the begining of the string, until it reaches the specified lenght
# if the value of len parameter is less than the lenght of the string, no filling is done 
txt = '50'
x = txt.zfill(10)
print(x)


# Check string
# To Check if a certain phrase or character present in string, we can use the keywords in or not in 

# Check if the phrase 'ain' is present in the following text
txt = 'The rain in the spain stays in the plain'
x = 'ain' in txt
print(x)

# Check the phrase 'ain' is not present in the following text
text = 'The rain in the spain stays in the plain'
x = 'ain' not in text
print(x)

# String concatenation
# To concatenate or to combine to strings you can use + operator
a = 'Hello'
b = 'World'
c = a + b
print(c)

# To add space between them, use ' ' 
a = 'hello'
b = 'world'
c = a +' ' + b
print(c)

# String format
# The format method formats the specified value and insert them inside the strings placeholder
# The placeholder is defined using curly brackets: { }
# As we learned in the python variables chapter, we cannot combine like this

age = 36
# txt = 'My name is John, I am ' + age

print(txt)

# But we can combine string and numbers using format() method
# The format method takes the arguments, formats them, and places them in the string
# where the placeholders { }:

age = 26
txt = 'My name is Rajendra, I am {}'
print(txt.format(age))

# The format method takes unlimited arguments, and are placed into respective placeholders
quatity = 3
itemno = 576
price = 49.95
myorder = 'I want {} pieces of item {} for {} dollars.'
print(myorder.format(quatity, itemno, price))

# we can use index numbers {0} to be sure the arguments are placed in the correct placeholders
quantity = 3
itemno = 567
price = 49.95
myorder = 'I want to pay {2} dollars for {0} pieces of item {1}.'
print(myorder.format(quantity, itemno, price))


# ljust
# the ljust method will left align the string, using a specified character as fill character
string = 'banana'
x = string.ljust(20)
print(x, 'is my favourite fruit')

# lstrip
# the lstrip method removes the leading characters in the string(space is the default character to remove)
txt = '  banana   '
x = txt.lstrip()
print("of all fruits", x, "is my favourite fruit")

txt = 'asdsdbanana'
x = txt.lstrip('asd')
print('of all fruits', x, "is my favourite fruit")


# rfind() finds the last occurence of the specified value
# It returns -1 if the value is not found
# It is almost same as the rindex()
txt = "welcome to my world"
x = txt.rfind("e")
print(x)

y = txt.rfind("e", 5, 10)
print(y)

# rindex
# searches the string and find the last occurence of the specifies value. it raises an exeception if the value is not found
txt = "welcome to my world"
x = txt.rindex("e", 5, 10)
print(x)

# rjust 
# the rjust() method will right align the string, using a specified character(space is default) as the fill character
txt = 'banana'
x = txt.rjust(20)
print(x)
 
# rpartition()
# The rpartition method searches for the last occurence of a specified string, and splits the string into a tuple containing
# three elements
# the first element contains the part before the specified string
# the second element conatains the specified string
# The third element contains the part after the string
txt = " I could eat bananas all day,  bananas are my favourite fruit"
x = txt.rpartition("bananas")
print(x)

# rstrip()
# rstrip method removes any trailing characters(characters at the end of a string), space is default trailing characters
# to remove
txt = "  banana  "
x = txt.rstrip()
print("of all fruits", x, "is my favourite fruit")

# rsplit()
# rsplit method split the string into list starting from the right
# if no max is specified, this method will return the same as the split() method
# When maxsplis is specified, this method will contain the specified number of elements plus one


txt = "apple, banana, cherry"
x = txt.rsplit(",")
print(x)

# title()
# title() method returns a string where the first character in every word is upper case. like header, or a title
# if the word contains a number or symbol, the first letter after that will be converted to upper case
txt = "Welcome to my second world"
x = txt.title()
print(x)

# Escape character that are illegal in a string, use an escape character.
# An escape character is a backslash \ followed by the character you want to insert 
# An example of an illegal character is a double quote inside a string that is surrounded by double quotes
txt = "We are the so called \"vikings\" from the north"

# Python operators
# operators are used to perform operations on variables and values
# python devides the operators in the following groups

# Arithematic operators
# Assignment operators
# Comparision operators
# Logical operators
# Identity opearators
# Membership operators
# Bitwise operators

# Python lists
# Python collections(Arrays)
# there are four collection data types in the python programing language
# LIST is a collection which is ordered and changeable. Allows duplicate members.
# TUPLE is a collection which is ordered and unchangeable. Allows duplicate members
# SET is a collection which is unordered and unindexed. No duplicate members
# DICTIONARY is a collection which is unordered, changeable and indexed. no duplicate members

# when choosing collection type it is useful to understand the properties of that type.
# choosing the right type for a perticular data set could mean retension of meaning 
# and it could mean increase the efficiency and security



































# PIP 
# What is PIP 
# PIP is a package manager for python packages , or modules if you like
# If you have python 3.4 later pip is included by default
# # What is package
# A package contains all the files you need for a module
# modules are code libraries you can include in your project
# check if pip is installed 
# Once package is installed you can use that package in your project
