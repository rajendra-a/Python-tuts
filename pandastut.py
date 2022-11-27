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

# Create your own lables
a = [1, 7, 3]
myvar2 = pd.Series(a, index= ['x', 'y', 'z'])

print(myvar2["y"])


# Key value objects as series
# You can also a key/value object, like dictionary, when creating series.

# Creat a simple Pandas Series from a dictionary:

calories = {'day1': 420, 'day2':380, 'day3':390}
myvar = pd.Series(calories)
print(myvar)

# DataFrames
'''
Data sets in Pandas are usually multi-dimensional tables, called DataFrames.
Series like a column, DataFrame is the whole table 
'''
# Create a dataframe from two series:
data = {
    'calories': [420, 380, 390],
    'duration':[50, 40, 45]
}

myvar = pd.DataFrame(data)
print(myvar)


# The keys of the dictionary become the labels
# To select only some of the items in the dictionary, use the index argument and specify only the items you want to include  in the series

# Create a series using only data from 'day1' 'day2'
myvar = pd.Series(calories, index=['day1', 'day2'])
print(myvar)

# Data sets in pandas are usually multi-dimentional tables, called DataFrames
# Series is like a column, a Data Frame is whole table
# 
# Create a DataFrame from two Series:
data = {
    'calories':[420, 380, 390],
    'duration': [50, 40, 45]
} 

myvar = pd.DataFrame(data)
print(myvar)


# What is data frame?
# A Pandas dataframe is a 2 dimentional data structure like a 2 dimentional array, or a table with rows and columns
# Create a simple pandas Dataframe

data = {
    'colories': [420, 380, 390],
    'duration': [50, 40, 45]
}

# load data into 
df = pd.DataFrame(data)

# Locate Row
'''
As you can see from the result above, The DataFrame is like a table with rows and columns 
Pandas use the loc attribute to return one or more specified rows
'''
print(df.loc[0])

print(df.loc[[0, 1]])


# Named indexes 
# With the index argument you can name your own indexes 

# Add a list of names to give each row a name:
data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}


df = pd.DataFrame(data, index=["day1", "day2", "day3"])
print(df)

# Locate Named indexes 
'''
Use the named index in the loc attribute to return the specified row(s)
return day2 
'''
print(df.loc['day2'])
print(df.loc[['day2', 'day3']])



# Load Files into a DataFrames 
# If your data sets are stored in a file, Pandas can load them into a DataFrame
# Load comma separated file (csv) into DataFrame.

df = pd.read_csv('consumers-price-index-numbers.csv')
print(df)

# Read CSV files 
# A Simple way to store big data sets is to use csv files 
# CSV files contains plain text and is well know format that can be read by everyone including pandas
# in out examples we will be using a csv fiel called 'data.csv'

# Load the csv into dataframe
df = pd.read_csv('data.csv')
print(df.to_string()) # use to_string() method to print entire dataframe


# If you have a large Dataframe with many rows, pandas only return the first 5 rows, and the last 5 rows
print(df)

# max rows 
# The number of rows returned is defined in Pandas option settings
# you can check your systems maximum rows with the pd.options.display.max_rows statement 
print(pd.options.display.max_rows)

# You can change the maximum rows number with the same statement

# Increase the maximum number of rows to display entire Dataframe
pd.options.display.max_rows = 9999
df = pd.read_csv('data.csv')
print(df)

# Read json
# Big datasets are often stored, or extracted as JSON
# JSON is plain text, but has the format of an object, 
# 
# In our examples we will be using JSON file called 'data.json'

# Load json file into a DataFrame

df = pd.read_json('data.json')
print(df.to_string())

# Dictionary as json
# JSON = Python dictionary
# If your json code is not in file, but in python dictionary, you can load it into a DataFrame Directly
# Load a python dictionary into dataframe
data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}

df = pd.DataFrame(data)
print(df)


# Pandas analyzing DataFrames
# Viewing the data

'''
One of the most used method for getting a quick overview of the DataFrame, is the head() method.
The head() method returns the headers and a specified number of rows, starting from the top 
'''
df = pd.read_csv('data.csv')
print(df.head(10))

# Print the first 5 rows of the DataFrame
df = pd.read_csv('data.csv')
print(df.head())

# There is also a tail() method for viewing the last rows of the DataFrame
# The tail() method returns the headers and a specified number of rows, starting  from the bottom

# Print last five rows of the DataFrame
print(df.tail())


# Info about the data
# The Dataframe object has a method called info(), that gives you more information about the data set.
print(df.info())


# Null values 
# The info() method also tells us how many non-null values  there are present in each column, and in our data set it seems like 
# there are 164 Non-Null values in the 'Calories' column.
# Which means That there are 5 rows with no value at all, in the calories, for  whatever reason
# Empty values, or Null values, can be bad when analyzing data, and you should consider removing rows with empty values. this is a step towards
# what is called cleaning data, and you will learn more about that in the next chapters

# Data cleaning means fixing bad data in your dataset.
# Bad data could be 
#  Empty cells
#  Data in Wrong format 
#  Wrong data 
#  Duplicates

# Empty Cells can potentially give you a wrong result when you analyze data.

# Remove Rows
# One way to deal with empty cells is to remove rows that contain empty cells 
# This is usually OK, since data sets can be very big, and removing a few rows will not have big impact on the result

df = pd.read_csv('data.csv')
new_df = df.dropna()
print(new_df.to_string())

# By default, the dropna() method returns a new DataFrame, and will not change the original
# If you want to change the original DataFrame, use the inplace=True argument:

df = pd.read_csv('data.csv')
df.dropna(inplace=True)
print(df.to_string())
 
# Note, the dropna(inplace = True) will NOT return a new DataFrame, but it will remove all rows containing NULL values from the original DataFrame.


# Remove all rows with NULL values
df = pd.read_csv('data.csv')
df.fillna(130, inplace=True)
print(df.to_string())


# Replace NULL values with the number 130
df = pd.read_csv('data.csv')
df.fillna(130, inplace=True)

# Replace only specified columns
# The example above replaces all empty cells in the whole DataFrame.
# To only replace empty values for one column, specify the column name for the DataFrame

# Replace empty values in the "Calories" columns with the number 130
df = pd.read_csv('data.csv')
df['colories'].fillna(130, inplace=True)


# Replace using mean median and mode
# A common way to replace empty cell, is to calculate the mean, median or mode value of the 
# Pandas uses the mean() median()  and mode() methods to calculate the respective values for a specified column

# Calculate the MEAN, and replace any empty values with it:
df = pd.read_csv('data.csv')
x = df['colories'].mean()

df['colories'].fillna(x, inplace=True)

# Mean The averge value(the sum of all values devided by number of values)

# Calculate the Median
df = pd.read_csv('data.csv')
x = df['colories'].median()
df['colories'].fillna(x, inplace=True)
# The value in the middle, after you have sorted all values searching
# Calculate the MODE, and replace any empty values with it.
df = pd.read_csv("data.csv")
x = df['colories'].mode()[0]
df['colories'].fillna(x, inplace=True)
# The value theat appears the most

# Pandas - Cleaning data of wrong format
# cells with data of wrong format can make it difficult,, or even impossible, to analyze data.
# To fix it, you have two options: removet the rows, or convert all cells 

# Convert into a Correct format
# In our Data Frame, we have two cells with the wrong format, checkout 
# Lets try to convert all cells in the 'Date' column into dates.
# pandas has to_date() method for this
df = pd.read_csv('data.csv')
df['Date'] = pd.to_datetime(df['Date'])
print(df.to_string())


# The result from the converting in the example above gave us a NaT value, which can be handled as a NULL value, and we can remove the row by
# using the dropna() method.

# Remove rows with a null value
df.dropna(subset=['Date'], inplace=True)

# Wrong data does not have to be 'empty cells' or 'wrong format', it can be just be wrong, like if someone registered '199'instead of '1.99'.
# sometimes you can spot wrong data by looking at the dataset, because you have an expectation of what should be.
# if you take a look at our data set, you can see that in row 7, the duration is 450, but for all the other rows the duration is between 30 and 60
# It doesn't have to be wrong, but taking in consideration that this is the data set of someone's workout sessions, we conclude with the fact that
# this person did not work out in 450 minutes

# Set duration = 45 in row 7
df.loc[7, "Duration"] = 45

# For small data sets you might be able to replace the wrong data one by one, but not for big data sets.
# To replace wrong data for larger data sets you can create some rules, e.g set some boundaries for legal values and replaces any values that are 
# outside of the boundaries
# Loop through all values in the "Duration column"
# If the value is higher than 120, set it to 120
for x in df.index:
  if df.loc[x, 'Duration'] > 120:
    df.loc[x, 'Duration'] = 120


# Removing rows
# Another way of handling wrong data is to remove the rows that contains wrong data.
# This way you do not have to find out what to replace them with, and there is a good chance you do not need them to do your analysis

# Delete rows where duration  is higher than 120
for x in df.index:
  if df.loc[x, 'Duration'] > 120:
    df.drop(x, inplace = True)

# To discover duplicates, we can use the duplicated() method.
# The duplicated() method returns a Boolean values for each row:
# Returns True for every row that is a duplicate, otherwise False

print(df.duplicatd())

# To remove duplicates, use the drop_duplicates()
# Remove all duplicates
df.drop_duplicates(inplace = True)



# Data Correlations
# Finding relationships
# corr() method  calulates the relationship between each column in your data set
# The examples in this page uses csv file called 'data.csv'
df.corr()
# The corr() method ignores 'not numeric' columns

# Result Explained 
# The Result of the corr() method is a table with a lot of numbers that represents how well the relationship is between two columns.
# The numbers varies from -1 to 1.
# 1 means that there is a 1 to 1 relationship, and for this data set, each time a value went up in the first column, the other one went up as well
# 0.9  is also a good ralationship, and if you increase one value, the other will probably go down
# -0.9 would be just as good relationship as 0.9, but as you increase one value, the other will probably go down
# 0.2 means not a good relationship, meaning that if one value goes up does not mean that the other will. 