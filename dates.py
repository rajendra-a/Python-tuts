# Python dates
# A date in python not a data type of its own, but we can import a module named datatime
# to work with dates as date objects
# import the current datetime module and display the current date:
import datetime
x = datetime.datetime.now()
print(x)

# Date output 
# when we exexute the code from the example above the result will be
# the date contains year, month, day, hour, minute, second, and micro second
# The datetime module has many methods to return information about the dateobject 
# here we can see few objects
import datetime 
x = datetime.datetime.now()
print(x.year)

print(x.strftime('%A'))


# Creating date object
# TO create date,, we can use the datetime() class of the datetime module 
# The datetime class require three parameters to create a date: year, month, day

x = datetime.datetime(2020, 5, 12)
print(x)

# The date time class also takes paremeters for time and timezone, but they are optional and 
# has default value of 0 

# The strftime method 
# the datetime object has method for formatting date objects into readable strings
# the method is called strftime, and takes one parameter, format to specify the format of the returned string

# display the name of the string
import datetime
x = datetime.datetime(2018, 5, 19)
print(x.strftime('%B'))
