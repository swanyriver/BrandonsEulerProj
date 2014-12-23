import brandonsEP
import itertools

primes = brandonsEP.sieve(10**7)

def replace(diglist, places, verbose=False):
    found = 0
    originalDigit = diglist[places[0]]
    for d in range(10):
        for i in places: diglist[i]=d
        if (  brandonsEP.binary_search(primes, brandonsEP.lsToNum(diglist))
          and diglist[0]):
            found+=1
            if verbose: print found, ":",brandonsEP.lsToNum(diglist)

    for i in places: diglist[i]=originalDigit
    return found

def search():
    for p in primes[primes.index(101):]:
        dig = brandonsEP.digits(p)
        for length in range(2,len(dig)):
          for combo in itertools.combinations(range(len(dig)), length):
              if all(dig[x]==dig[combo[0]] for x in combo):
                score = replace(dig, combo)
                #print score
                #print a,b, p, score,  dig[a],dig[b], dig
                if score==8: 
                  replace(dig, combo, verbose=True)
                  return p

#print replace([5,6,0,0,3], 2, 3)
print search()