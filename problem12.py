import math

curtriang =0
nextAdd = 0
while True:
    nextAdd+=1
    curtriang+=nextAdd

    numFactors=0
    for f in xrange(1,int(math.sqrt(curtriang))):
        if not curtriang%f:
            numFactors+=2
    if not curtriang%int(math.sqrt(curtriang)):
        numFactors  -=1
    if numFactors>500:
        print curtriang
        break
    #print curtriang, " factors:",numFactors
