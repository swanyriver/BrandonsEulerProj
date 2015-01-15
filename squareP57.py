import brandonsEP

def expansion(terms):
    n,d = 3,2

    for x in range(terms):
        yield (n,d)
        n,d = n+d*2,d+n

total = 0

for exp in expansion(1000):
    n,d = exp
    if brandonsEP.lengthNum(n)>brandonsEP.lengthNum(d): total+=1

print total
