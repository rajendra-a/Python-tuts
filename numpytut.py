'''
NumPy is a python library, is used for working with arrays, and is short name for numerical python
It also has functions for working in domain of linear algebra, fourier transform and matrices
In Python we have lists that server the purpose of the arrays, but they are slow to process
Numpy aims to provide an array object that is up to 50x faster than python traditional lists
the array object in numpy called ndarray, it provides a lot of supporting functions that make working with ndarray very easy
Data Science: where we study how to store, use and analyse data for deriving information from it.
'''
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)

print(np.__version__)



# create numpy ndarray object
'''The array object in nunpy is called ndarray, we can create a numpy ndarray object by using the array() function'''
print(type(arr))

#Dimentions in array
'''
0 dimentional arrays, or scalars, are the elements in an array. Each value in an array is a 0-D array
Create a 0-D array with value 42
'''
arr1 = np.array(42)
print(arr1)
'''
1-D Arrays
An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array
These are the most common and basic arrays 
'''
arr2 = np.array([1, 2, 3, 4, 5, 6])
print(arr2)

'''
2-D arrays  
An array that has 1-D arrays as its elements is called 2-D array
'''
arr3 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr3)

'''
3-D arrays
An array that has 2-D arrays as its elements is called 3-D array
'''
arr4 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9],[10, 11, 12]]])

''' Check number of Dimentions
NumPy arrays provides the ndim attribute that returns an integer that tells us how many dimentions the array have
'''
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)
print(arr4.ndim)

'''
Array indexing is the same as accessing an array element.
you can access an array element by referring to its index number.
The indexes in Numpy arrays start with 0, meaning that the first element has index 0, and the second has index 1 etc.
'''

print(arr[0])
print(arr[1])

print(arr[2] + arr[3])

'''
Access 2-D arrays 
To access elements from 2-D arrays we can use comma separated integers representing the dimention and the index of the element.
Think of 2-D arrays like a table with rows and columns, where the row represents the dimension and the index represents the column.
Access the element on the first row and second columns, where the row reprents the dimension and column represents the index.
'''
arr5 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print('2nd element on 1st row:  ', arr5[0, 1])


print('5th element on 2nd row: ', arr5[1, 4])

'''
Access 3-D arrays 
To access elements from 3-D arrays we can use comma separated integers representing the dimensions and the index of the element.
Access the third element of the second array
'''

arr6 = np.array([[[1, 2, 3], [4, 5, 6]], [[8, 9, 10], [11, 12, 13]]])
print(arr6[0, 1, 2])

'''
Negative Indexing 
Use negative indexing for accessing elements from the end
'''

arr7 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print('last element from 2nd dim: ', arr7[1, -1])

# Slicing in Python
'''Slicing means taking elements from one given index to another given index.
We pass slice instead of index like this [start:end]
We can also define the step, like this [start:end:step].
If we don't pass start its considered 0
If we don't pass end its considered length of the array in that demention
If we don't pass step its considered as 1
'''

# Slice elements from index 1 to 5 from the following array:
arr8 = np.array([1, 2, 3, 4, 5, 6])
print(arr8[1:5])

print(arr8[1:])

print(arr8[:4])

# Negative slicing

'''
Use the negative operator to refer to an index from the end
Slice from the index 3 from the end to index 1 from the end
'''
print(arr8[-3:-1])

'''Use the step value to determine the step of the slicing
Return every other element from index 1 to index 5'''

arr9 = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr9[1:5:2])

'''
Return every other element from the entire array
'''
arr10 = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr10[::2])

'''
Slicing 2-D array
From the second element, slice elements from  index 1 to  index 4
'''
arr11 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr11[1, 1:4]) # Remember that second element has index 1

'''
From both elements return index 2
'''
print(arr11[0:2, 2])

# From both elements, slice index 1 to index 4, this will return 2-D array:
print(arr11[0:2, 1:4])


# Data types in Numpy
'''
Numpy has some extra data types
By default python have these data types
strings- Used to represent text data, the text is given under quote marks. e.g. "ABCD"
integer- Used to represent integer numbers. e.g. -1, -2, -3.
float- Used to represent real numbers. e.g. 1.0, 42.42
boolean- Used to represent the complex numbers. e.g. 1.0 + 2.0j, 1.5+ 2.5j    

Below is list of data types in Numpy and the characters used to represent them.
i - integer
b - boolean
u - unsingned integer
f- float
c- complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
v - Fixed chunk of memory for other type
''' 
# Checking the data type of an array 
''' The Numpy array object has a property called dtype that returns the array'''
arr11 = np.array([1, 2, 3, 4 ])
print(arr.dtype)

arra12 = np.array(['apple', 'banana', 'cherry'])
print(arra12.dtype)

# Creating the data type using defined array type
'''
we use array function can take optional argument: dtype that allows us to define the expected data type of the  array elements:
for i, u, f, S, U we can define the size as well 
'''
arr13 = np.array([1, 2, 3, 4], dtype='S')
print(arr13)
print(arr13.dtype)

# What if a value can not be converted 
'''
If a type is given in which elements can't be casted then Numpy will raise a ValueError.
A not integer string like 'a' can not be converted to integer (will raise an error).
'''
# arr14 = np.array(['a', '1', '2'], dtype='i')

'''
The best way to change the data type of exsting array, is to make a copy of the array with the astype() method.
The astype() function creates a copy of the array, and allows you specify the data type as a parameter.
The data type can be specified using a string, like 'f' for float, 'i' for integer etc. or you can use the data type directly like float for
float and int fot integers
'''
# change data type from float to integer by using 'i' as parameter value
arr15 = np.array([1, 2, 3, 4, 5, 6])
newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)

'''
change data type from float to integer by using int as a parameter value
'''
arr16 = np.array([1.2, 3.5, 5.7])
newarr2 = arr16.astype(int)
print(newarr2)
print(newarr2.dtype)

# change data from int to bool

arr17 = np.array([1, 3, 0])
newarr3 = arr17.astype(bool)
print(newarr3)
print(newarr3.dtype)

# The difference between Copy and View 
'''
The main difference between copy and view of an array is that the copy is a new array , and the view is just a view of original array.
The copy owns the data and any changes made to the copy will not effect the original array, and any chages made to the original array will not 
effect the copy.
The view doesn't own the data and any changes made to the view will effect the original array, and any changes made to the original array will effect the 
view.
'''

# make a copy, change the original array, and display both arrays
arr18 = np.array([1, 2, 3, 4, 5])
z = arr18.copy()

arr18[0] = 42
print(arr18)
print(z)

'''
The copy should not be effected by the changes made to orignal array
'''
# VIEW 
'''
Make a view, and change the original array, and display both arrays 
'''

arr19 = np.array([1, 2, 3, 4, 5, 6, 7])
x = arr19.view()
arr19[0] = 43
print(arr19)
print(x)

'''The original array should be effected by the changes made to view'''
# Check if array owns its data 
'''
As mentioned above, copies owns the data, and views doesn't own the data, but how can we check this?
Every Numpy array has the attribute base that returns None if the array owns the data
otherwise the base attribute refers to the original object 
'''
arr20 = np.array([1, 2, 3, 4, 5])
s = arr20.copy()
r = arr20.view()

print(s.base)
print(r.base)

'''
The copy returns None
The view returns the original array. 
'''

# Shape of an array

'''
The shape of an array is the number of elements in each dimention. 
'''

# Get the shape of an array
'''
Numpy arrays have an attribute called shape that returns a tuple with each index having the number of corresponding elements.
'''
# print the shape of a 2-D array
arr21 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr21.shape)

'''
The example above returns (2, 4), which means that the array has two dimensions, where the first dimension has 2 elements and second has 4 
'''

'''create array with 5 dimensions using ndmin using veactor of values   1, 2, 3, 4 and verify that last dimension has value 4.
'''

arr22 = np.array([1, 2, 3, 4], ndmin=5)
print(arr22.shape)


# What does the shape tuple represent
'''
Integers at every index tells about number of elements the corresponding dimention has.
In the example above at the index-4 we have value 4, so we can say that 5th (4 + 1 th) dimention has 4 elements
'''


# Reshaping arrays
'''
Reshaping means changing the shape of array.
The shape of an array is the number of elements in each dimention.
By reshaping we can add or remove dimensions or change number of elements in each dimension.     
'''

# Reshaping From 1-D array with 12 elements into 2-D array.
'''Convert the following 1-D array with 12 elements into 2-D array.
The outermost dimension will have 4 arrays, each with 3 elements
'''
arr23 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr4 = arr23.reshape(4, 3)
print(newarr4)

# Reshape from 1-D to 3-D
newarr5 = arr23.reshape(2, 3, 2)
print(newarr5)


# Can we reshape into any shape?
'''
Yes, as long as the elements required for reshaping are euqal in both shapes 
We can reshape an eight elements 1D array into 4 elements in 2 rows 2-D array but we cannot reshape it into a 3 elements 3 rows 2-D array as that would
require 3*3 = 9 elements
'''

# newarr6 = arr23.reshape(3, 3) 
# print(newarray6)
# Returns copy or view
'''
Check if the returned array is a copy or a view: 


'''

newarr7 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(newarr7.reshape(2, 4).base)

# The example above returns the original array, so it is a view

# Unknown Dimension
'''
You are allowed to have one 'unknown' dimension.
Meaning that you do not have to specify an exact number for one of the dimensions in the reshape method
pass -1 as the value, and numpy will calculate this number for you.
'''

# Convert 1-D array with 8 elements to 3D array with 2X2 elements
arr24 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr8 = arr24.reshape(2, 2, -1)
print(newarr8)
# we cannot pass more than one dimension    
# Flattening the arrays
'''
Flattening array means converting a multidementional array into a 1D array.
we can use reshape(-1) to do this. 
'''

arr25 = np.array([[1, 2, 3], [4, 5, 6]])
newarr9 = arr25.reshape(-1)
print(newarr9)


# Numpy array iterating
'''
Iterating arrays. Iterating means going through elements one by one.
As we deal with multi-demensional array in numpy, we can do this using basic for loop
If we iterate on a 1-D array it will go through each element one by one'''

# Iterate on a 1-D array it will go through each element one by one

arr30 = np.array([1, 2, 3])
for x in arr30:
    print(x)
'''
Iterate on the elements of the following 2-D array: 
'''
arr31 = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr31:
    print(x)

'''
If we iterate on a n- Dimentional array it will go through n-1th dimension one by one
to return scalars, the actual values we have to iterate the arrays in each dimension 
'''
arr32 = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr32:
    for y in x:
        print(y)

'''
Iterate on 3-D array  
'''

arr32 =  np.array([[[1, 2, 3],[4, 5, 6], [7, 8, 9], [10, 11, 12]]])
for x in arr32:
    print(x)

# iterate down to the scalars

for x in arr32:
    for y in x:
        for z in y:
            print(z)

'''
Iterating arrays using nditer()
The function nditer() is a helping function that can be used from very basic to very advance iterations. It solves some basic issues
which we face in iteration, lets go through it with examples 
In basic for loops, iterating through each scalar of an array we need to use n for loops which can be difficult to write for arrsays with very 
high dimensionality 
'''

# iterate through the following 3-D array:
arr33 = np.array([[[1,2], [3, 4], [5, 6], [7, 8]]])
for x in np.nditer(arr33):
    print(x)
    
print(arr33.ndim)
print(arr33.shape)

'''
Iterate array with diffrent data types
we cab use op_dtypes argument and pass it the expected datatype to change the datatype of elements while iterating
Numpy does not change the data type of the element in place so it needs some other space to perform this action, that extra space is called
buffer, and in order to enable it in nditer() we pass flags = ['buffered]
'''

arr34 =  np.array([1, 2, 3])
for x in np.nditer(arr34, flags=['buffered'], op_dtypes=['S']):
    print(x)

'''
Iterating with different step size 
'''
arr35 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in np.nditer(arr35[:, ::2]):
    print(x)

#Enumerated iteration using ndenumerate()
'''
Enumeration means mentioning sequence number of somethings one by one.
Sometimes we require corresponing index of the element while iterating, the ndenumerate method can be used for those use cases
'''
# enumerate 1-D array
arr35 = np.array([1, 2, 3])
for idx, x in np.ndenumerate(arr35):
    print(idx, x)

# Enumerate 2-D array
arr36 = np.array([[1, 2, 3], [4, 5, 6]])
for i, v in np.ndenumerate(arr36):
    print(i, v)


# Numpy joining array
'''
Joining means putting contents of two or more arrays in a single array.
In SQL we join tables based on a key, whereas in Numpy we join arrays by axes.
We pass a sequence of arrays that we want to join to the concatenate() function, along with the axis, if the axis is not explicitly passed,
It is taken as 0  
'''

arr37 = np.array([1, 2, 3])
arr38 = np.array([4, 5, 6])
arr39 = np.concatenate((arr37, arr38))
print(arr39)


# Join two 2-D arrays along rows(axis=1)

arr40 = np.array([[1, 2, 3], [4, 5, 6]])
arr41 = np.array([[7, 8, 9], [10, 11, 12]])

arr56 = np.concatenate((arr40, arr41))
print(arr56)

arr42 = np.concatenate((arr40, arr41), axis=1)
print(arr42)

# Joining arrays with stack Functions
'''
Stacking is same as concatenation, the only difference is that stacking is done along new axis.
We can concatenate two 1-D arrays along the second axis which would result in putting them one over the other, ie. stacking.
We pass a sequence of arrays that we want to join to the stack() method along with the axis. If axis is not explicitly passed it is taken as 0 
'''

# Stacking along rows

arr44 = np.array([1, 2, 3])
arr45 = np.array([4, 5, 6])

arr55 = np.stack((arr44, arr45), axis=1)
print(arr55)

arr46 = np.hstack((arr44, arr45))
arr47 = np.vstack((arr44, arr45))
print(arr46)
print(arr47)



 



# array splitting
'''
Splitting is reverse operation of Joining
Joiing merges multiple arrays into one and Splitting breaks one array into multiple.
We use array_split() for splitting arrays, we pass it the array we want to split and the number of splits
'''

# Split the array in  3 parts
arr48 = np.array([1, 2, 3, 4, 5, 6])
arr49 = np.array_split(arr48, 3)

print(arr49)

# If the array has less elements than required, it will adjust from the end accordingly
# Split the array in 4 parts

arr50 = np.array_split(arr48, 4)


'''
We also have split() method available but it will not adjust the elements when elements are less in source array 
for splitting like in example above, array_split()  worked properly but split() would fail
'''

# Split into arrays
'''
The return value of the array_split() method is an array containing each of the split as an array.
If you split an array into 3 arrays, you can access them from the result just like any array element.
'''

# Access the split arrays
arr51 = np.array([1, 2, 3, 4, 5, 6])
arr52 = np.array_split(arr51, 3)

print(arr52[0])
print(arr52[1])
print(arr52[2])

'''
Splitting 2-D arrays
Use the same syntax when splitting 2-D arrays
Use the array_split() method, pass in the array you want to split and the number of splits you want to do  
'''
# split the 2-D arrays into 2-D arrays

arr53 = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
arr54 = np.array_split(arr53, 3)
print(arr54)


# Another example, this time each element in the 2-D arrays contains 3 elements
arr58 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
arr59 = np.array_split(arr58, 3)
print(arr59)


# In addition, you can specify which axis you want to do the split around
# the example below also returns three 2-D arrays, but they are split along the row (axis=1)
arr60 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
arr61 = np.array_split(arr60, 3, axis=1)
print(arr61)

# The alternative method is using hsplit() which is opposite of hstack()
# Use the hsplit() method to split the 2-D array into three 2-D arrays along rows

arr62 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
arr63 = np.hsplit(arr62, 3)
print(arr63)

arr64 = np.vsplit(arr62, 3)
print(arr64)

# Searching arrays  

'''
You can search an array for a certain value and return the indexes that get a match
to search an array, use the where() method'''

# Find the indexes where the value is 4:
arr65 = np.array([1, 2, 3, 4, 5, 6, 4, 4])
x = np.where(arr65 == 4)
print(x)

# Return a a tuple of indexes
# Find the indexes where the values are even

arr66 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = np.where(arr66%2 == 1)
print(y)

# Searchsorted 
'''
There is a method called searchsorted() which performs a binary search in the array, and returns the index where the specified value would be inserted
to inserted to maintain the search order 
'''

# Find the indexes where the value 7 should be inserted
arr_new1 = np.array([6, 7, 8, 9])
x = np.searchsorted(arr_new1, 7)
print(x) 

# Example explained: The number 7 should be inserted on index 1 to ramain the sort order
# The method starts the search from the left and returns the first index where the number 7 is no longer larger than the next value

# Search from the right side 
# By default left most index is returned, but we can give side='right'
# find the indexes where the value 7 should be inserted, starting from the right

arr_new2 = np.array([6, 7, 8, 9])
x = np.searchsorted(arr_new2, 7, side="right")
print(x)
# Example explained: the number 7 should be inserted on index2  to remain the sort order.
# The method starts the search from the right and returns the first index where the number 7 is no longer less than the next value.

# Multiple values

# to search for more than one value, use an array with the specified values.
# Find the indexes where the values 2, 4 and 6 should be inserted  
arr_new3 = np.array([1, 3, 5, 7])
x = np.searchsorted(arr, [2, 4, 6])
print(x)

# The return value is an array: [1, 2, 3] contaning the three indexes where 2, 4, 6 would be inserted in the original array to maintain the order
# Numpy sorting arrays
'''
sorting means putting elements in an ordered sequence
Ordered sequence is any sequence that has an order corresponding to elements, numeric or alphabetical, ascending or descending.
The Numpy ndobject has a function called sort(), that will sort the specified array
'''

# sort the array
arr67 = np.array([3, 2, 1, 0])
print(np.sort(arr))

# the above method returns a copy of array, leaving the original array
'''
you can also sort arrays of strings, or any other data type 
'''

# sort the array alphabetically
arr68 = np.array(['banana', 'cherry', 'apple'])
print(np.sort(arr68))


# Sort a boolean array
arr69 = np.array([True, False, False])
print(np.sort(arr69))

# Sorting a 2-D array
arr70 = np.array([[3, 2, 4], [5, 0, 9]])
print(np.sort(arr70))




# Fitering Arrays
'''
Getting some elements out of an existing array and creating a new array out of them is calling is filtering
In numpy, you filter an array using a boolean index list.
If the value at index is True that element is contained in the filtered array, if the value at index is false that element is 
excluded from the filtered array
'''

arr71 = np.array([41, 42, 43, 44])
x = [True, False, True, False]
arr72 = arr71[x]
print(arr72)


# The example above will  return [41, 43]  because the new array only values where the filer array had the value of true, in this case index 0 and 2
# Creating the filter array 
# In the example above we hard-coded the True and False values, but the common use is to create a filer array based on conditions.
# Create filter array that will return only values higher than 42:

arr73 = np.array([41, 42, 43, 44])
filter_array = []
for element in arr73:
# if the element is higher than 42, set the value to True, Otherwise False
    if element > 42:
        filter_array.append(True)
    else:
        filter_array.append(False)

arr74 = arr73[filter_array]
print(filter_array)
print(arr74)

# Create filter array that will return only even elements from the original 
# The above example is quite a common task in numpy and numpy provides a nice way to tackle it
# We can directly substitute the array instead of the iterable variable in our condition and it will work just as we expect it to.

# Create filter array that will return only values higher than 42:
arr75 = np.array([41, 42, 43, 44])
arr76 = arr75 > 42
arr77 = arr75[arr76]
print(arr76)
print(arr77)