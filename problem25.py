import math


def digits(x):
    return int(math.log10(x)+1)


f1 = 1
f2 = 1
temp = 0
term = 2
LIMIT = 1000

while True:
    term +=1
    temp = f1
    f1 += f2
    f2 = temp
    #print term, ":", f1, digits(f1)
    if digits(f1) >= LIMIT:
        #print f1
        print term
        break

