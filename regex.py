# Python regex or python regular expression, is a sequence of characters that form a search pattern
# Regex can be used to check if a string contains a specified search pattern
# Regex module 
# Python has builtin module called re, which can be used to work with regular expressions
# Import the re module
import re 
# when you have imported the re module, you can start using regular expressions
# Search the string that starts with The and ends with spain
import re
txt = "The rain in spain"
x = re.search("^The.*spain$", txt)

print(x)

# The findall function 
# The findall function returns list containin all matches 
# print list of all matches
import re
str = "The rain in spain"
x = re.findall('ai', str)
print(x)

# the list contains matches in the order they are found
# If no matches are found an empty list is returned

# return an empty list if no match was found
import re
str = 'The rain in spain'
x = re.findall('portugal', str)
print(x)


#the serch() function
# The search function searches the string for a match and returns a match object
# if there is a match, only the first occurence of the match will be returned

# search for white space character
str = 'The rain in spain'
x = re.search('\s',str)
print('The first white space character is located in position:', x.start())

# The split function
# The split function returns a list where the string has been spllit at each match
# split at each white space character
import re
str = "The rain in spain"
x = re.split('\s', str)
print(x)

# you can control the number of occurences by specifying the maxsplit parameter
# split the string only at the first occurence
import re
str = 'The rain in spain'
x = re.split("\s", str, 1)
print(x)

# The sub() function
# The sub() function replaces the matches with the text of your choice
# Replace every white space character with the number 9
import re
str = 'The rain in spain'
x = re.sub('\s', '9', str)
print(x)

# You can control the number of replacements by specyfying count parameter
# replace the first two occurences
import re 
str1 = 'The rain in spain'
x = re.sub('\s', 9, str1, 2)
print(x)
# Match object
# A match object is an object containing information about search and result

# if there is no match none will be returned, instead of match object
# DO a search that will be returned a match object
import re
str = 'The rain in spain'
x = re.search('ai', str)
print(x)

# The match object has properties and methods used to retrieve information about search,and
# the result
# .span() method returns tuple containing start, end positions of the match
# .string() return the string passed into the function
# .group() return the part of the string where there was a match

# print the position of the first match occurence
# The regular expression looks for anywords that starts with uppercase S
import re
str = 'The rain in the spain'
x = re.search(r'\bS\w+', str)
print(x.span())


# print the string passed into the function
str = 'The rain in spain'
x = re.search(r'\bS\w+', str)
print(x.string)

#print the part of a string where there was a match
#The regular expression looks for any words that starts with an upper case "S"

import re
str = 'The rain in the spain'
x = re.search(r'\bS\w+', str)
print(x)