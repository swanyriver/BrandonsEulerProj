import brandonsEP

digFacts = [brandonsEP.fact(x) for x in range(10)]
print digFacts

sumI = 0
for i in range(10,50000):
    if int(sum([digFacts[int(k)] for k in brandonsEP.digits(i)])) == i:
        print i
        sumI += i

print "my result", sumI