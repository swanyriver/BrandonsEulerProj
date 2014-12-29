import math

def isPent(num):
    n = math.sqrt(24*num+1) + 1
    d = divmod(n,6)
    return not d[1]

def isTri(num):
    n = math.sqrt(8*num+1) + 1
    d = divmod(n,2)
    return not d[1]

def ishex(num):
    n = math.sqrt(8*num+1) + 1
    d = divmod(n,4)
    return not d[1]

def tri(n):
    return n*(n+1)//2

#x = tri(285)
#print isPent(x), ishex(x)

for n in range(286,10**6):
    x = tri(n)
    if isPent(x) and ishex(x):
        print n, x
        break
