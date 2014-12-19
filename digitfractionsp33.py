discoverd = []
epsilon = .00005
for a in range(1,9):
    for b in range(a+1,10):
        for c in range(1,10):
            fract = a/float(b)
            ca = a + c*10
            ac = a*10 + c
            cb = b + c*10
            bc = b*10 + c

            if abs(ca/float(cb) - fract)<epsilon:
                discoverd.append(((a,b),(ca,cb)))

            if abs(ca/float(bc) - fract)<epsilon:
                discoverd.append(((a,b),(ca,bc)))

            if abs(ac/float(cb) - fract)<epsilon:
                discoverd.append(((a,b),(ac,cb)))

            if abs(ac/float(bc) - fract)<epsilon:
                discoverd.append(((a,b),(ac,bc)))

print discoverd
numProduct = discoverd[0][1][0]
divproduct = discoverd[0][1][1]
print numProduct, divproduct
for pair in [x[1] for x in discoverd[1:]]:
    numProduct*=pair[0]
    divproduct*=pair[1]
print numProduct, " over ",divproduct

from brandonsEP import allDivisors

divN = allDivisors(numProduct)
divD = allDivisors(divproduct)


gcd = max([x for x in divN if x in divD])

print max(divN)
print [x for x in divN if x in divD]

print numProduct/gcd
print divproduct/gcd