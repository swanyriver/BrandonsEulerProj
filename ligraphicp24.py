import itertools

pm = itertools.permutations(range(10))

onepm = ()

for i in xrange(10**6):
    onepm = pm.next()

print onepm
answer = ""
for num in onepm:
   answer+=str(num)

print answer


###  manual calculation
def fact(x):
    if x==1: return x
    else: return x*fact(x-1)

nums = range(10)

answer=""

rem = 10**6
for f in range(9,0,-1):
    smaller = divmod(rem,fact(f))
    print rem, smaller, f, fact(f), nums
    rem = smaller[1]
    answer+= str(nums.pop(smaller[0]))

print answer

