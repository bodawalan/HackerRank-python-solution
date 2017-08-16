import sys
import os
from math import *
from collections import *


def  getMinimumUniqueSum(arr):
    a_1 = []
    for i in arr:
        a = float(ceil(sqrt(i)))
        a_1.append(a)

    b = [item for item, count in collections.Counter(a_1).items() if count > 1]
    return len(b)+1



    return arr



f = open(os.environ['OUTPUT_PATH'], 'w')

_arr_cnt = 0
_arr_cnt = int(input())
_arr_i = 0
_arr = []
while _arr_i < _arr_cnt:
    _arr_item = str(input())
    _arr.append(_arr_item)
    _arr_i += 1

res = getMinimumUniqueSum(_arr);
for res_cur in res:
    f.write(str(res_cur) + "\n")

f.close()


""" find the square root element of gibe range
Input:
2
3 9
17 24

output:
2 
0

Explaination:
here between 3 nd 9 square root element is only 2 which is 4 and 9 so "2"
same 17 and 24 no root element there
"""