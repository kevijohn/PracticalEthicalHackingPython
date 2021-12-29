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