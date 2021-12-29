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

nl()
# Relational and Boolean Operators
greater_than = 7 > 5
less_than = 5 < 7
greater_than_equal_to = 7 >= 7
less_than_equal_to = 7 <= 7

test_and = (7 > 5) and (5 < 7)
test_and2 = (7 > 5) and (5 > 7) 
test_or = (7 > 5) or (5 < 7)
test_or2 = (7 > 5) or (5 > 7)

test_not = not True

print(test_and, test_and2, test_or, test_or2, test_not)

nl()
# Conditional Statements
def drink(money):
    if money >= 2:
        return "You've got yourself a drink."
    else:
        return "No drink for you."

print(drink(3))
print(drink(1))

def alcohol(age, money):
    if age >= 21 and money >= 5:
        return "We're getting a drink!"
    elif age >= 21 and money < 5:
        return "Come back with more money."
    elif age < 21 and money >= 5:
        return "Nice try, kid!"
    else:
        return "You're too poor and too young."

print(alcohol(21, 5))
print(alcohol(21, 4))
print(alcohol(20, 4))

nl()
# Lists - Have brackets []
movies = ["When Harry Met Sally", "The Hangover", "The Perks of Being A Wallflower", "The Exorcist"]

print(movies[1]) # Returns the second item
print(movies[0]) # Returns the first item
print(movies[1:4])
print(movies[1:])
print(movies[:2])
print(movies[-1]) # Get last item
movies.append("Jaws") # Adds to the end of the list
print(movies)

movies.pop() # removes last item
print(movies)

movies.pop(0) # removes first item
print(movies)

# tuples are immutable
# lists are mutable

nl()
# Tuples - Do not change, ()
grades = ('a', 'b', 'c', 'd', 'f')
print(grades[1])

nl()

# Looping

# for loops - start to finish of an iterate
vegetables = ['cucumber', 'spinach', 'cabbage']
for x in vegetables:
    print(x)

# while loops - Execute as long as true

i = 1

while i < 10:
    print(i)
    i += 1
