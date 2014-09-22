# Conditionals Examples

# Return True if year is a leap year, false otherwise
def is_leap_year(year):
    if (year % 400) == 0:
        return True
    elif (year % 100) == 0:
        return False
    elif (year % 4) == 0:
        return True
    else:
        return False


year = 2012
leap_year = is_leap_year(year)
    
if leap_year:
    print year, "is a leap year"
else:
    print year, "is not a leap year"