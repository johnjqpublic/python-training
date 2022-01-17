"""
Functions

Author: 
Date:   
"""

# The objective of this exercise is to become familiar 
# with using functions in Python

# I recommend reading this first
# https://www.w3schools.com/python/python_functions.asp

# Here is a dictionary of aircraft carriers
# The 'key' is the hull number and the 'value' is another dictionary which should be self-explanatory
aircraft_carriers = {65:{'name':'USS ENTERPRISE',           'class':'ENTERPRISE', 'comm_date':'11/25/1961', 'decomm_date':'02/03/2017'},\
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

# Write a function that accepts two string dates as arguments 
# and returns the number of years between the dates rounded to the nearest year
# Here's a hint: https://docs.python.org/3.8/library/datetime.html

def calculate_years(start_date, end_date):
    import datetime

    #FIXME: finish this!

    # Return the answer
    return


# The code below loops over the 'aircraft_carriers' dictionary 
# and runs your function
# https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/
if __name__ == "__main__":
    print('')

    # Iterate over the dictionary of aircraft carriers
    for ship in aircraft_carriers:
        # Calculate the years of service of the carrier
        years_of_service = calculate_years(aircraft_carriers[ship]['comm_date'], aircraft_carriers[ship]['decomm_date'])

        #TODO: come up with a way to print the results in an easily readable manner

    print('')

# Congratulations! You have completed the lesson on functions
