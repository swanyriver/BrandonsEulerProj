import brandonsEP
from math import factorial

limit = 10**6
length = 60
count = 0

def sumfact(num):
    return sum(map(factorial,brandonsEP.digits(num)))

def makeSeris(x):
    seris = [x] + [sumfact(x)]
    while seris[-1] not in seris[:-1]:
        seris.append(sumfact(seris[-1]))
    return seris

#cyclers = [145,169,363601,1454,871,872,45361,45362]



for x in range(1,limit):
    if len(makeSeris(x))==length+1:
        count +=1

print count