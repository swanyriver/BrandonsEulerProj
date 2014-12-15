from brandonsEP import allDivisors

LIMIT = 10000

sd = {i:sum(allDivisors(i)) for i in xrange(2,LIMIT)}

pairs = []

for key in sd:
    v = sd.get(key)
    if sd.get(v) == key and key!=v: pairs.append(key)

print pairs
print sum(pairs)