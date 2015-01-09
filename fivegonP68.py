gonSize = 5
setSize = gonSize*2

import brandonsEP, itertools
from mydigitInt import digitInt


magicGons = []

for gon in itertools.permutations(range(1,setSize+1)):
    innergon = gon[-gonSize:]
    outtergon = gon[:gonSize]
    sums  = [gon[i] + innergon[i] + innergon[(i+1)%gonSize] for i in range(gonSize)]
    if all(sums[0] == sumi for sumi in sums):
        #we have magic
        #print min(outtergon), outtergon.index(min(outtergon)), gon
        num = []
        start = outtergon.index(min(outtergon))
        for i in range(gonSize):
            index = (i+start)%gonSize
            num.append(gon[index])
            num.append(innergon[index])
            num.append(innergon[(index+1)%gonSize])
        #print gon, num
        #print gon, num
        #print reduce(brandonsEP.concatNums,num)
        magicGons.append(reduce(brandonsEP.concatNums,num))

magicGons = [digitInt(x) for x in magicGons]
magicGons = filter(lambda x:len(x)<=16, magicGons)

print max(magicGons), len(max(magicGons))


