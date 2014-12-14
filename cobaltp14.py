def cobalt(n):
    if not n%2:
        return n/2
    else:
        return 3*n+1


seed = 10**6-1
#seed = 20
print seed
lengths = {}

for x in xrange(seed,1,-1):
    num = x
    stack = []
    while True:
        stack.append(num)
        discovered = lengths.get(num,1)
        if discovered!=1 or num==1:
            leng = discovered
            while len(stack):
                lengths[stack.pop()]=leng
                leng+=1
            break
        num = cobalt(num)



#print lengths

longest = max(lengths)
print "pahtlength:", longest
print "seed:", lengths.get(longest)