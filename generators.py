# Python generators
# Generator function: A generator is defined like normal function
# But whenever it needs to generate  a value , it does so with the yield keyword rather than 
# return. if the body of def contains yield, thr function automatically generator function

def simple_generaration():
    yield 1
    yield 2
    yield 3

for value in simple_generaration():
    print(value)

# Generator object 
# Generator function return generator object. generator objects are used either by calling the next
# methodon generator object or using the generaotor object in a for loop
def simplegenratorfun():
    yield 1
    yield 2
    yield 3

x = simplegenratorfun()
# print(x.next())

# A simple program for fibonacci series using generator
def fib(limit):

    # initali first two fibonacci numbers
    a, b = 0, 1

    # one by one yield fibonacci numbers

    while a < limit:
        yield a
        a, b = b, a+b

x = fib(5)
#print(x.next())


# iterating over generator object using for

for i in fib(5):
    print(i)