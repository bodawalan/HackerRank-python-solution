"""Vrroom!
OK, now let's add a method named run_lap. It'll take a length argument. It should reduce the fuel_remaining attribute by length multiplied by 0.125.
Oh, and add a laps attribute to the class, set to 0, and increment it each time the run_lap method is called."""



def combiner(list1):
    sum1 = 0
    string = ""
    for i in list1:
        if isinstance(i, int) or isinstance(i, float) :
            sum1 += i
        elif isinstance(i, str):
            string += i
    print( "{}{}".format(string, sum1))

combiner(["ni",3.5,4])