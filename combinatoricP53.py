from brandonsEP import numCombs as cnr


count = 0
for n in range(23,101):
    for r in range(2,n//2):
        if cnr(n, r) > 10**6: count+=2
    if cnr(n, n//2) > 10**6:
        if n&1: count+=2
        else: count+=1

print count 