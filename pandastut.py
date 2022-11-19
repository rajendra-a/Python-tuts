# Pandas
# pandas is a python library used to work with datasets
# It has functions for analyzing, cleaning, exploring, and manipulating data.
# The name pasdas has a reference to both 'Panel data', and 'Python Data Analysis' and was created by wes mikinney in 2008

# Why use pandas 
# Pandas allows us to analyze big data and make conslusions based on statistical theories.
# Pandas can clean messy data sets, and make them readable and relevant.
# Relevant data is very important in data science


# what pandas can do?
# Pandas gives you answers about the data like:
# Is there a correlation between two or morw columns
# What is average value
# max value
# min value
# Pandas also able to delete rows that are not relavant, or contains wrong values, like empty or NULL values. this is called cleaing data.
# Pandas as pd
import pandas as pd
mydataset = {
    'cars':['BMW', 'Volo', 'Ford'],
    'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)

# Checking padas version
print(pd.__version__)

# Series 
# A Pandas series is like a column in a table.
# It is one dimentional array holding data of any type
# Create a simple pandas from list

a = [1, 7, 2]
myvar1 = pd.Series(a)
print(myvar1)

# Labels
'''
If nothing else is specified, the values are labeled with their index number. First value has index 0, second value has index 1 etc
this label can be used to access a specified value.
'''
# Return the first value of the series 
print(myvar1[0])

# Create labels
# With the index argument, you can name your own labels.

