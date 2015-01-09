import brandonsEP
from mydigitInt import digitInt

poly = brandonsEP.polynumber

#generate lists of 4 digit figurate numbers

seprateFigs = []

for s in range(3,9):
    subFig = []
    next = digitInt(0)
    n = 1
    while len(next)<5:
        next = digitInt(poly(s,n))
        n+=1
        if len(next)==4: subFig.append(next)
    seprateFigs.append(subFig)

def combine(x,y):
    x.extend(y)
    return x

for i in range(len(seprateFigs)):
    seprateFigs[i] = [(x,i) for x in seprateFigs[i]]

allFigs = sorted(reduce(combine, seprateFigs))
print allFigs

def findCycl(numSet, currentSet, index, output):
    for i in range(index,len(numSet)):
        if numSet[i][:2] == currentSet[-1][-2:]:
            findCycl(numSet, currentSet[:]+[numSet[i]], i+1, output)
    output.append(currentSet)

def findCycl2(numSet, currentSet, index, output, polysUsed):
    for i in range(index,len(numSet)):
        if numSet[i][0][:2] == currentSet[-1][-2:] and numSet[i][1] not in polysUsed:
            print currentSet, polysUsed
            findCycl2(numSet, currentSet[:]+[numSet[i][0]], i+1, output, polysUsed[:]+[numSet[i][1]])
    output.append(currentSet)

orderedCyclicles=[]


#needs to be recursive
for index in range(len(allFigs)):
    findCycl2(allFigs, [allFigs[index][0]], index+1, orderedCyclicles, [allFigs[index][1]])

orderedCyclicles = filter(lambda x:len(x)>4, orderedCyclicles)

print orderedCyclicles, len(orderedCyclicles)
print sum(orderedCyclicles[0])