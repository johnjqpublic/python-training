"""
Working With Lists

Author: 
Date:   
"""

# The objective of this exercise is to become familiar 
# with working with Python lists

# I recommend reading this first
# https://docs.python.org/3.8/tutorial/introduction.html#lists

# Here is a list of aircraft carriers
aircraft_carriers = ['USS ENTERPRISE',\
                     'USS NIMITZ',\
                     'USS DWIGHT D. EISENHOWER',\
                     'USS CARL VINSON',\
                     'USS THEODORE ROOSEVELT',\
                     'USS ABRAHAM LINCOLN',\
                     'USS GEORGE WASHINGTON',\
                     'USS JOHN C. STENNIS',\
                     'USS HARRY S. TRUMAN',\
                     'USS RONALD REAGAN',\
                     'USS GEORGE H. W. BUSH']

#NOTE: The '\' character breaks input across lines
#NOTE: This can be useful to improve the readability of code

# Start by printing the entire list to see what it looks like



# Print only the first item in the list
# Remember, Python indexes begin at zero



# Assuming you didn't know how long the list is,
# print the last item in the list



# Now let's say that you want to know how long the list is
# The len() function returns the length of a list
# https://docs.python.org/3.8/library/functions.html#len



# There's a carrier missing from the list!
# Add USS GERALD R. FORD to the end of the list 
# and then print the updated list



# Now there's too many carriers in the list!
# Remove USS ENTERPRISE from the list 
# and then print the updated list



# Use the len() function to count how many carriers 
# are currently in the fleet



# Python lists also have a .sort() method which can be used to sort the list
# https://docs.python.org/3.8/howto/sorting.html
# Sort the list of aircraft carriers and print the result



# Lists in Python can contain mixes of data types
# Here is an example of a list that contains a string, 
# two integers, and a floating point number
mixed_data = ['Uranium', 92, 143, 235.043924]

# Use the mixed_data list to print the following sentence
# "Uranium 235 has an atomic weight of 235.043924"



# Here's a neat trick
# The .split() method converts a string into a list of strings
# https://docs.python.org/3.8/library/stdtypes.html?highlight=split#str.split
# Split and rearrange the following string into "Public, John Q."
name = 'John Q. Public'



# Here's another neat trick
# The 'pretty-print' module can be used to print lists in a nice format
# https://docs.python.org/3.8/library/pprint.html
# Try it out on the 'aircraft_carriers' list
import pprint



# Here is another list of aircraft carriers
# This time it is a list of lists
#   The 1st entry in the inner list is the ship's hull number
#   The 2nd entry in the inner list is the ship's name
#   The 3rd entry in the inner list is the ship's commissioning date (if applicable)
#   The 4th entry in the inner list is the ship's decommissioning date (if applicable)
aircraft_carriers_new = [[65, 'USS ENTERPRISE',           '11/25/1961', '02/03/2017'],\
                         [68, 'USS NIMITZ',               '05/03/1975',  False],\
                         [69, 'USS DWIGHT D. EISENHOWER', '10/18/1977',  False],\
                         [70, 'USS CARL VINSON',          '03/13/1982',  False],\
                         [71, 'USS THEODORE ROOSEVELT',   '10/25/1986',  False],\
                         [72, 'USS ABRAHAM LINCOLN',      '11/11/1989',  False],\
                         [73, 'USS GEORGE WASHINGTON',    '07/04/1992',  False],\
                         [74, 'USS JOHN C. STENNIS',      '12/09/1995',  False],\
                         [75, 'USS HARRY S. TRUMAN',      '07/25/1998',  False],\
                         [76, 'USS RONALD REAGAN',        '07/12/2003',  False],\
                         [77, 'USS GEORGE H. W. BUSH',    '01/10/2009',  False],\
                         [78, 'USS GERALD R. FORD',       '07/22/2017',  False],\
                         [79, 'PCU JOHN F. KENNEDY',       False,        False]]

# You don't need to do anything with this list unless you want to
# Feel free to experiment

# Here's a basic example of how to address an element of a list within a list
print(''); print(aircraft_carriers_new[0][1]); print('')
#NOTE: Semi-colons can be used to separate multiple commands on the same line



# Congratulations! You have completed the lesson on lists
