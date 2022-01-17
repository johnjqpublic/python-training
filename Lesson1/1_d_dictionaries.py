"""
Working With Dictionaries

Author: 
Date:   
"""

# The objective of this exercise is to become familiar 
# with working with Python dictionaries

# I recommend reading this first
# https://docs.python.org/3.8/tutorial/datastructures.html#dictionaries

# Here is a dictionary of aircraft carriers
# The 'key' is the hull number and the 'value' is the name
aircraft_carriers = {65:'USS ENTERPRISE',\
                     68:'USS NIMITZ',\
                     69:'USS DWIGHT D. EISENHOWER',\
                     70:'USS CARL VINSON',\
                     71:'USS THEODORE ROOSEVELT',\
                     72:'USS ABRAHAM LINCOLN',\
                     73:'USS GEORGE WASHINGTON',\
                     74:'USS JOHN C. STENNIS',\
                     75:'USS HARRY S. TRUMAN',\
                     76:'USS RONALD REAGAN',\
                     77:'USS GEORGE H. W. BUSH'}

#NOTE: The '\' character breaks input across lines
#NOTE: This can be useful to improve the readability of code

# Start by printing the entire dictionary to see what it looks like



# Pick your favorite carrier and print only its entry in the dictionary



# There's a carrier missing from the dictionary!
# Add USS GERALD R. FORD to the dictionary 
# and then print the updated dictionary



# Now there's too many carriers in the dictionary!
# Remove USS ENTERPRISE from the dictionary 
# and then print the updated dictionary



# Here's another neat trick
# The 'pretty-print' module can be used to print dictionaries in a nice format
# Try it out on the 'aircraft_carriers' dictionary
import pprint



# Here is another dictionary of aircraft carriers
# This time the 'key' is the hull number and the 'value' is a list
# (i.e., a dictionary of lists)
#   The 1st entry in the list is the ship's name
#   The 2nd entry in the list is the ship's commissioning date (if applicable)
#   The 3rd entry in the list is the ship's decommissioning date (if applicable)
aircraft_carriers_new = {65:['USS ENTERPRISE',           '11/25/1961', '02/03/2017'],\
                         68:['USS NIMITZ',               '05/03/1975',  False],\
                         69:['USS DWIGHT D. EISENHOWER', '10/18/1977',  False],\
                         70:['USS CARL VINSON',          '03/13/1982',  False],\
                         71:['USS THEODORE ROOSEVELT',   '10/25/1986',  False],\
                         72:['USS ABRAHAM LINCOLN',      '11/11/1989',  False],\
                         73:['USS GEORGE WASHINGTON',    '07/04/1992',  False],\
                         74:['USS JOHN C. STENNIS',      '12/09/1995',  False],\
                         75:['USS HARRY S. TRUMAN',      '07/25/1998',  False],\
                         76:['USS RONALD REAGAN',        '07/12/2003',  False],\
                         77:['USS GEORGE H. W. BUSH',    '01/10/2009',  False],\
                         78:['USS GERALD R. FORD',       '07/22/2017',  False],\
                         79:['PCU JOHN F. KENNEDY',       False,        False]}

# You don't need to do anything with this dictionary unless you want to
# Feel free to experiment

# Here's a basic example of how to address an element of a list within a dictionary
print(''); print(aircraft_carriers_new[65][0]); print('')
#NOTE: Semi-colons can be used to separate multiple commands on the same line



# Here is yet another dictionary of aircraft carriers
# This time the 'key' is the hull number and the 'value' is a dictionary which should be self-explanatory
# (i.e., a dictionary of dictionaries)
aircraft_carriers_new_new = {65:{'name':'USS ENTERPRISE',           'class':'ENTERPRISE', 'comm_date':'11/25/1961', 'decomm_date':'02/03/2017'},\
                             66:{'name':'USS AMERICA',              'class':'KITTY HAWK', 'comm_date':'01/23/1965', 'decomm_date':'08/09/1996'},\
                             67:{'name':'USS JOHN F. KENNEDY',      'class':'KENNEDY',    'comm_date':'09/07/1968', 'decomm_date':'08/01/2007'},\
                             68:{'name':'USS NIMITZ',               'class':'NIMITZ',     'comm_date':'05/03/1975', 'decomm_date':False},\
                             69:{'name':'USS DWIGHT D. EISENHOWER', 'class':'NIMITZ',     'comm_date':'10/18/1977', 'decomm_date':False},\
                             70:{'name':'USS CARL VINSON',          'class':'NIMITZ',     'comm_date':'03/13/1982', 'decomm_date':False},\
                             71:{'name':'USS THEODORE ROOSEVELT',   'class':'NIMITZ',     'comm_date':'10/25/1986', 'decomm_date':False},\
                             72:{'name':'USS ABRAHAM LINCOLN',      'class':'NIMITZ',     'comm_date':'11/11/1989', 'decomm_date':False},\
                             73:{'name':'USS GEORGE WASHINGTON',    'class':'NIMITZ',     'comm_date':'07/04/1992', 'decomm_date':False},\
                             74:{'name':'USS JOHN C. STENNIS',      'class':'NIMITZ',     'comm_date':'12/09/1995', 'decomm_date':False},\
                             75:{'name':'USS HARRY S. TRUMAN',      'class':'NIMITZ',     'comm_date':'07/25/1998', 'decomm_date':False},\
                             76:{'name':'USS RONALD REAGAN',        'class':'NIMITZ',     'comm_date':'07/12/2003', 'decomm_date':False},\
                             77:{'name':'USS GEORGE H. W. BUSH',    'class':'NIMITZ',     'comm_date':'01/10/2009', 'decomm_date':False},\
                             78:{'name':'USS GERALD R. FORD',       'class':'FORD',       'comm_date':'07/22/2017', 'decomm_date':False},\
                             79:{'name':'PCU JOHN F. KENNEDY',      'class':'FORD',       'comm_date':False,        'decomm_date':False}}

#NOTE: If you like that then you'll probably be a fan of pandas DataFrames

# You don't need to do anything with this dictionary unless you want to
# Feel free to experiment

# Here's a basic example of how to address an element of a dictionary within a dictionary
print(''); print(aircraft_carriers_new_new[68]['name']); print('')
#NOTE: Semi-colons can be used to separate multiple commands on the same line



# Congratulations! You have completed the lesson on dictionaries
