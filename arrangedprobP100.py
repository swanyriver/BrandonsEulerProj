import itertools, brandonsEP,math

for n in itertools.count(start=1000):
    #print n

    d = n**2-n
    
    blue_discs = int(math.ceil(math.sqrt(d>>1)))

    if blue_discs**2 - blue_discs == d>>1 :
        #1/2 probability
        print "blue_discs:",blue_discs, " red: ", n-blue_discs ," total discs:", n
        #break
