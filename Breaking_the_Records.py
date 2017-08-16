"""Sample Input 0

9
10 5 20 20 4 5 2 25 1
Sample Output 0

2 4


Explanation 0

The diagram below depicts the number of times Maria 
broke her best and worst records throughout the season:

image

She broke her best record twice (after games 2 and 7) and her worst record four times (after games 1,4 , 6, and 8),
so we print 2 4 as our answer. Note that she did not break her record for best score during game ,
 as her score during that game was not strictly greater than her best record at the time.

#https://www.hackerrank.com/challenges/breaking-best-and-worst-records"""


score_list=[3,4,21,36,10,28,35,5,24,42]
print(sorted(score_list))

ls=hs=score_list[0]
lc=hc=0
for score in score_list:
    if (score > hs):
        hs=score
        hc += 1
    if (score<ls):
        ls = score
        lc += 1

print(hc,lc)
