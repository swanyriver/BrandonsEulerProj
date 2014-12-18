import itertools
import math

def extractNums(x):
    nums = []
    while(x>0):
        div = divmod(x,10)
        nums.append(div[1])
        x = div[0]
    nums.reverse()
    return nums


POW = 5

raised = [x**POW for x in range(10)]

MAX = raised[-1]*POW

discovered = []

for combolength in range(2,POW+4):
    combos = itertools.combinations_with_replacement(range(10),combolength)

    for cmb in combos:
        s = sum([raised[i] for i in cmb] )

        digits = extractNums(s)

        digits.sort()
        #print cmb, s, digits
        if len(digits)==combolength and all([digits[i]==cmb[i] for i in range(len(digits))]):
            discovered.append(s)

print discovered
print sum(discovered)
