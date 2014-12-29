import brandonsEP

def isLychrel(num):
    for iteration in xrange(1,50):
        dlist = brandonsEP.digits(num)
        rd = list(reversed(dlist))
        if dlist == rd and iteration!=1:
            return False
        num = num + brandonsEP.lsToNum(rd)
        #print dlist, rd, rd == dlist, num + brandonsEP.lsToNum(rd)
    else:
        return True

#test = [196,349,47,10677]
#for n in test: print n, isLychrel(n)
lychcount = 0

for x in xrange(10000): lychcount+=isLychrel(x)
print lychcount