user_list_one=list(map(int,input("enetr the number in list").split()))
user_list_two=list(map(int,input("enetr the number in list").split()))
# it only works for same size list
if len(user_list_one) == len(user_list_two):

    print([i for i,j in zip(user_list_one,user_list_two) if i==j])
# it will work with unequal length of list
else:
    print([x for x in user_list_one if x in user_list_two])



lines=[lines[0:(lines[i].find('(') - 1) ]for i in range(len(lines))if (lines[i].find('(')) != -1]

