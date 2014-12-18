import itertools


c = itertools.combinations_with_replacement(range(2,101),2)


distinct = set()

for combo in c:
    distinct.add(combo[0]**combo[1])
    distinct.add(combo[1]**combo[0])


print len(distinct)