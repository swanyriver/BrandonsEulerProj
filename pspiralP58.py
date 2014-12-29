import brandonsEP

def spiral(loc,layer):
    result = []
    for x in range(4):
        loc+=layer
        result.append(loc)
    return result

loc = 1
sp =[]
numP = 0
diags = 1

for layer in range(2,10**9,2):
    sp.extend(spiral(loc, layer))
    loc = sp[-1]

    for x in sp[-4:]: 
        if brandonsEP.isPrime(x): numP+=1

    diags +=4
    ratio = numP / float(diags)
    if ratio<.1:
        print layer+1
        break



# print sp
# print [x for x in sp if brandonsEP.isPrime(x)]

# print sp[-4:]
# p = 0
# for x in sp[-4:]: 
#     if brandonsEP.isPrime(x): p+=1
# print p