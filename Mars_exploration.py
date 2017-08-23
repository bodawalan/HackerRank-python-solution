import re
s="OOSDSSOSOSWEWSOSOSOSOSOSOSSSSOSOSOSS"

count=0

for x,y in zip(s,'SOS'*33):
    if x!=y:
        count +=1

print(count)

print(zip(s,'SOS'*33))