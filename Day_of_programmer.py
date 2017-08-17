year=1700
leap_year_sum=244
non_leap_year_sum=243
if ((year % 4 == 0) and (year % 100 !=0)) | (year % 400==0):
    print("{}.09.{}".format(256 - leap_year_sum,year))
else:
    print("{}.09.{}".format(256 - non_leap_year_sum, year))

"""
import sys

def solve(year):
    if (year == 1918):
        return '26.09.1918'
    elif ((year <= 1917) & (year%4 == 0)) or ((year%400 == 0) or ((year%4 ==0) & (year%100 != 0))):
        return '12.09.%s' %year
    else:
        return '13.09.%s' %year

                


year = int(input().strip())
result = solve(year)
print(result)

"""

#https://www.hackerrank.com/challenges/day-of-the-programmer/problem