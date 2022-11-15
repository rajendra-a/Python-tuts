# # Module
# Consider a module to be the same as code library
# A file containing set of functions you want to include in your application 

# Create module
# To create module just save the code you want in a file with fiel extension .py

# now we can use the module we just created by using import statement
# import the module
import mymodule
mymodule.greeting('rajendra')

# when usig function from module use syntax module.function
# varibles in modules the module can contain functions as already described but also variables of all types

a = mymodule.person1['age']
print(a)

# import only dictionary person1 from the module
from mymodule import person1
print(person1['age'])

# When importing from keyword, do not use the module name when reffering to elements in the module
