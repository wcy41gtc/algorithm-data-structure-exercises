# This short program demostrates a function that calculates the days between given dates

def isLeapYear(year):
    """
    Determine if the year is leap year:
    Definition of leap year: https://en.wikipedia.org/wiki/Leap_year
    Args:
        year (int): year
    Returns:
        bool: true for leap year, false for not leap year
    """
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

def daysInMonth(year, month):
    """
    Determine how many days in a given month of the year

    Args:
        year (int): year
        month (int): month

    Returns:
        days (int): number of days in the month of the year
    """
    if month in [1, 3, 5, 7, 8, 10, 12]:
        days = 31
    if month in [4, 6, 9, 11]:
        days = 30
    if month == 2:
        if isLeapYear(year):
            days = 29
        else:
            days = 28
    return days

def nextDay(year, month, day):
    """
    Returns the year, month, day of the next day.
    
    Args:
        year (int): year
        month (int): month
        day (int): day

    Returns:
        year (int): year
        month (int): month
        day (int): day
    """
    days = daysInMonth(year, month)
    if day < days:
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1

def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """
    Returns True if year1-month1-day1 is before 
    year2-month2-day2. Otherwise, returns False.

    Args:
        year1 (int): year
        month1 (int): month
        day1 (int): day

        	year2 (int): year
        month2 (int): month
        day2 (int): day

    Returns:
        Bool:  True if year1-month1-day1 is before year2-month2-day2, False if year1-month1-day1 is not before year2-month2-day2
    """
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """
    Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar.
    """
       
    # Throw an AssertionError if the input is not valid
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days

def codeTest(year1, month1, day1, year2, month2, day2, answer):
    try:
        result = daysBetweenDates(year1, month1, day1, year2, month2, day2)
        if result == answer and answer != "AssertionError":
            return True
        else: 
            return False
    
    except AssertionError:
        if answer == "AssertionError":
            return True
        else:
            return False

def main():
    test = []
    #1
    test.append(codeTest(2012,1,1,2012,2,28,58))
    #2
    test.append(codeTest(2012,1,1,2012,3,1,60))
    #3
    test.append(codeTest(2011,6,30,2012,6,30,366))
    #4
    test.append(codeTest(2013,1,1,1999,12,31, "AssertionError"))
    #5
    test.append(codeTest(2011,1,1,2012,8,8,585))
    #6
    test.append(codeTest(1991,3,1,1991,1,3,"AssertionError"))
    #7
    test.append(codeTest(2012,2,1,2012,3,1,29))
    #8
    test.append(codeTest(1900,1,1,1999,12,31,36523))

    if False in test:
        print("Test {} failed".format(test.index(False)+1))
    else:
        print("All tests passed!")

if __name__ == "__main__":
    main()