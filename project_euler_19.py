"""
    Project Euler 19: Counting Sundays

    You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

    How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

import time
from math import floor

def get_day_of_week(year, month, day):
    """
    Return the week day for the day indicated by day/month/year

    :param year:
    :param month:
    :param day:
    :return: the week day i.e. Sunday (0) to Saturday (6)
    """

    """
    Gaussian algorithm to determine day of week
    https://en.wikipedia.org/wiki/Determination_of_the_day_of_the_week#Disparate_variation
    
    w = (d + floor(2.6*m-0.2) + y + floor(y/4) + floor(c/4) - 2*c) mod 7
    
    Y is the year minus 1 for January or February, and the year for any other month
    y is the last 2 digits of Y
    c is the first 2 digits of Y
    d is the day of the month (1 to 31)
    m is the original month number shifted by 2 (March=1, ... , February=12)
    w is the day of week (0 = Sunday, ... ,6 = Saturday). If w is negative you have to add 7 to it.
    """

    m = (month - 3) % 12 + 1
    if m > 10:
        Y = year - 1
    else:
        Y = year
    y = Y % 100
    c = (Y - (Y % 100)) / 100
    d = day

    # Disparate Gaussian algorithm
    w = (d + floor(2.6 * m - 0.2) + y + floor(y / 4) + floor(c / 4) - 2 * c) % 7

    return int(w)

def months_start_range(target_day, year_start, year_end):
    """
    Compute the number of times a target day is the first of a month.

    :param target_day: the day (Monday, Tuesday, ... Sunday)
    :param year_start:
    :param year_end:
    :return: Number of times the target_day is the first of a month
    """
    total = 0

    for year in range(year_start, year_end + 1):
        for month in range(1, 13):
            # If target_day is the first day of a month
            if get_day_of_week(year, month, 1) == target_day:
                total += 1

    return total

start = time.time()
# Counting the number of Sundays, i.e. 0, in first day of the month
result = months_start_range(0, 1901, 2000)
elapsed = time.time() - start

print("Number of Sundays as the first day of a month is {0} found in {1:.8f} seconds".format(result, elapsed))