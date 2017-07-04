def sleep_in(talking,hour):
    if  (talking and hour<7) or (talking and hour>20):
        return True
    else:
        return False

result=sleep_in(talking=True,hour=7)
print(result)

