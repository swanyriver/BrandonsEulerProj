import brandonsEP, collections

def pow3():
    n = 1
    while True:
        yield n**3
        n+=1


numlength = 0
perms = collections.defaultdict(list)

for x in pow3():
    if brandonsEP.lengthNum(x)>numlength:
        #print filter(lambda x:len(x)>2, perms.values())
        for ls in perms.values():
            if len(ls)==5:
                print min(ls)
                exit()
        numlength = brandonsEP.lengthNum(x)
        perms.clear()
    k = brandonsEP.lsToNum(sorted(brandonsEP.digits(x)))
    perms[k].append(x)


