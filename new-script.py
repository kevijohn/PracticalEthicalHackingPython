# Author: Kevin Johnson
# Created: DEC 29 2021

import sys # system functions and parameters
from datetime import datetime as dt # import with alias

print(dt.now())
#print(sys.version)

my_name = 'Kevin'
print(my_name[0])
print(my_name[-1])

sentence = "This is a sentence"
print(sentence[:4])

print(sentence.split())

sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split)
print(sentence_join)

quote = "He said, \"Give me all your money\""
print(quote)

too_much_space = "                  hello               "
print(too_much_space.strip())

print('a' in 'Apple') # is case-sensitive

letter = 'A'
word = 'Apple'
print(letter.lower() in word.lower()) # Improved

movie = "Aliens"
print("My favorite movie is {}".format(movie))

# Dictionaries - key/value pairs {}
drinks = {"White Russian": 7, "Old Fashion": 10, "Lemon Drop": 8} # Drink is the key, price is the value
print(drinks)

employees = {"Finance": ['Bob', 'Linda', 'Tina'],
"IT": ['Gene', 'Louise', 'Teddy'], "HR": ['Jimmy Jr.', 'Mort']}
print(employees)

employees['legal'] = ['Mr. Frond']
print(employees)

employees.update({"Sales": ['Andie', 'Ollie']})
print(employees)

drinks['White Russian'] = 8
print(drinks)

print(drinks.get("White Russian"))