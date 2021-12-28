# Author: Kevin Johnson
# Created: DEC 28 2021

# Variables and Methods
quote = "All is fair in love and war"
print(quote.upper()) # upper case
print(quote.lower()) # lower case
print(quote.title()) # title case

print(len(quote))

name = "Kevin" # string
age = 43 # int
gpa = 2.4 # float

print(int(age))
print(int(43.9)) # int does not round

print("My name is " + name + " and I am " + str(age) + " years old.")

age += 1
print(age)

birthday = 1
age += birthday
print(age)

print('\n')
# Functions
print("Here is an example function:")

def who_am_i():
    name = "Kevin"
    age = 30
    print("My name is " + name + " and I am " + str(age) + " years old.")

who_am_i()

# Adding parameters
def add_one_hundred(num):
    print(num + 100)

add_one_hundred(100)

# Multiple parameters
def add(x, y):
    print(x + y)

add(7,7)

def multiply(x,y):
    return x * y

print(multiply(7,7))

def square_root(x):
    print(x ** .5)

square_root(64)

def nl():
    print('\n')

nl()

# Boolean expressions (True or False)
print("Boolean Expressions:")

bool1 = True
bool2 = 3*3 == 9
bool3 = False
bool4 = 3*3 != 9

print(bool1, bool2, bool3, bool4)
print(type(bool1))
