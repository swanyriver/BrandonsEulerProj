import math

def pent(max = 10**6):
    n = 1
    while n<max:
        yield n * (3*n-1)//2
        n+=1


def isPent(num):
    n = math.sqrt(24*num+1) + 1
    d = divmod(n,6)
    return not d[1]

def check(pentnum):
    for prev in pent(i):
        if isPent(pentnum - prev) and isPent(pentnum+prev):
            print prev, pentnum
            print "D=", pentnum - prev
            return True
    return False

for i in xrange(1,10**6):
    pentnum = i * (3*i-1)//2
    if check(pentnum):
        break
