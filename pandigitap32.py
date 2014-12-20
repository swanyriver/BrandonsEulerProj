import brandonsEP
import math
dig = brandonsEP.digits

PDIGS = range(1,10)
products = []

def length(num):
    return int(math.log10(num))+1

for multA in [x for x in range(1,10000) if x%10]:
    digitsA = dig(multA)

    if length(multA**2)>9: break

    for multB in [x for x in range(multA,10000) if x%10]:
        prod = multA*multB

        if (len(digitsA) + length(multB) + length(prod))>9: break


        allDigs = digitsA + dig(multB) + dig(prod)
        allDigs.sort()
        #print allDigs, multA, multB
        #if allDigs == PDIGS[:len(allDigs)]:
        if allDigs == PDIGS:
            print allDigs, multA, multB, prod
            products.append(prod)

products.sort()
products = list(set(products))
print products
print sum(list(set(products)))

# b is sorted list of product and multipliers
# a is range(1,10)
# b == a[:len(b)]
