"""
Working With Strings

Author: 
Date:   
"""

# The objective of this exercise is to become familiar 
# with working with strings in Python

# I recommend reading this first
# https://docs.python.org/3.8/tutorial/introduction.html#strings

# Here is a string variable
can = 'Spam'

# Start by using the variable 'can' to print how you feel about Spam
# e.g., "Spam musubi is delicious!"



# Next, we'll get into indexing and slicing
# The diagram below illustrates the structure of a Python string
# It has indices for the position of each character,
# as well as indices for the positions between characters

#    0   1   2   3  <- Character Indices
#  +---+---+---+---+
#  | S | P | A | M |
#  +---+---+---+---+
#  0   1   2   3   4  <- Slice Indices
# -4  -3  -2  -1

# Use string slicing to print any words you can come up with 
# using the letters in the variable 'can'
# Try slicing both forwards and backwards



# Here's a neat trick
# If you have an input filename (of arbitrary length) 
# that you'd like to use as the output filename with a different extension, 
# split the string from the end to remove the extension and replace it with the new extension
# Try it on the variable below by replacing '.in' with '.out'
filename_in = 'really_important_file.in'



# Congratulations! You have completed the lesson on strings
