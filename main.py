"""
Import the "math" module. Then, print an alphabetically sorted list of all the functions available in the "math" module that start with the letters "is".
"""
# YOUR CODE HERE
import math

functions = dir(math)
# print(functions)

# as for loop / if statement
for word in functions:
  if word.startswith("is"):
    print(word)

# as list comprehension with if statement
print([word for word in functions if word.startswith("is")])