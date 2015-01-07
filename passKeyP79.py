f = open("keylog.txt")
keys = []
for line in f:
    key = []
    for c in line[:-1]: key.append(int(c))
    keys.append(key)

#print keys
#print any(keys)

keyphraseLength=0
keyphrase = 0
counts = [0]*10
for key in keys:
    counts[key[0]]+=1

#print counts.index(max(counts))

while any(keys):
    next = counts.index(max(counts))
    keyphrase*=10
    keyphrase+=next
    counts[next]=0
    keyphraseLength+=1
    for key in keys:
        print key

        if not key or key[0]!=next:continue
        del key[0]
        if key: counts[key[0]]+=1
        
    print next, counts

print keyphrase
print keyphraseLength

    