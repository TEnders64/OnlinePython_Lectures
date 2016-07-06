def oddEven():
    for num in range(1,2000+1):
        if num % 2 == 0:
            print "The number {} is even".format(num)
        else:
            print "The number "+str(num)+" is odd"

oddEven()
