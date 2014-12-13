import math
Nnumbers = 100

sumof = 0
sumsquares = 0

sumof = sum(range(1,Nnumbers+1))
print sumof
for each in range(1,Nnumbers+1):
    sumsquares += math.pow(each,2)
print sumsquares
print math.pow(sumof,2) - sumsquares
