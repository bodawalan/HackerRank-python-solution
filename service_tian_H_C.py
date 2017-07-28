import sys
import os

"""def  kSub( k,  nums):
    # it's in python 2 and it's own input we have chango accoring to their input ok?
    # if you want you remove this?
    total_list = 0
    total_nums = len(nums)
    for count in range(1, total_nums):
        for outer in range(0, total_nums-count):
            loop = 0
            sum = 0
            while loop<count:
                sum += nums[outer+loop]
                loop += 1
            if sum%k==0:
                #print("loop "+str(loop)+" outer "+str(outer))
                total_list += 1


    return total_list"""


def canReach(x1, y1, x2, y2):
    lst = [[x1, y1]]
    index = 0
    isreached = False
    while isreached == False and index < len(lst):
        subindex = lst[index]
        xs = subindex[0]
        ys = subindex[1]
        if xs == x2 and xs + ys == y2:
            isreached = True
            return "Yes"
        if xs + ys == x2 and ys == y2:
            isreached = True
            return "Yes"

        if xs + ys <= x2 or xs + ys <= y2:
            lst.append([xs + ys, ys])
            lst.append([xs, xs + ys])
        index += 1
    return "No"


f = open(os.environ['OUTPUT_PATH'], 'w')

_x1 = int(input());

_y1 = int(input());

_x2 = int(input());

_y2 = int(input());

res = canReach(_x1, _y1, _x2, _y2)
f.write(res + "\n")

f.close()








#-----------------balanced_______
import sys
import os


def balancedOrNot(expressions, maxReplacements):
    total_expression = len(expressions)
    res_output = []
    for index in range(total_expression):
        expression = expressions[index]
        maxReplacement = maxReplacements[index]
        if expression != None:
            checked = 0
            openindex = 0
            while expression.find("<", openindex) > 0:
                openindex = expression.find("<")
                closeindex = expression.find(">", openindex)
                if openindex < 0:
                    openindex = len(experession)
                    continue
                if closeindex != -1:
                    expression = expression[0:openindex] + expression[openindex + 1:closeindex] + expression[
                                                                                                  closeindex + 1:]
                    #                 else:
                    #                     expression = expression[0:openindex]+expression[openindex+1:]
            total_repl = 0
            while total_repl < maxReplacement:
                index = expression.find(">")
                if index >= 0:
                    expression = expression[0:index] + expression[index + 1:]
                total_repl += 1
            if expression.find("<") == -1 and expression.find(">") == -1:
                res_output.append(1)
            else:
                res_output.append(0)
                # res_output.append(maxReplacement)
        else:
            res_output.append(0)  ## as there are no replacements so after
            # any number of replacements it will be zero
    return res_output


f = open(os.environ['OUTPUT_PATH'], 'w')

_expressions_cnt = 0
_expressions_cnt = int(input())
_expressions_i = 0
_expressions = []
while _expressions_i < _expressions_cnt:
    try:
        _expressions_item = str(input())
    except:
        _expressions_item = None
    _expressions.append(_expressions_item)
    _expressions_i += 1

_maxReplacements_cnt = 0
_maxReplacements_cnt = int(input())
_maxReplacements_i = 0
_maxReplacements = []
while _maxReplacements_i < _maxReplacements_cnt:
    _maxReplacements_item = int(input());
    _maxReplacements.append(_maxReplacements_item)
    _maxReplacements_i += 1

res = balancedOrNot(_expressions, _maxReplacements)
for res_cur in res:
    f.write(str(res_cur) + "\n")

f.close()



