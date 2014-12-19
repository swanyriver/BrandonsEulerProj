from string import maketrans
fileName = "poker.txt"

pfile = open(fileName)

allHands = pfile.read()

outtab = ""
for i in range(1,6): outtab+=chr(ord('9')+i)
transtab = maketrans("TJQKA",outtab)
allHands = allHands.translate(transtab)

allHands = allHands.split('\n')
del allHands[-1]


def getRank(hand):
    flush,straight = False,False

    #hand= string 15 chars, 5 cards
    suits = [hand[x] for x in range(1,16,3)]
    cards = sorted([hand[x] for x in range(0,15,3)])

    if all([x==suits[0] for x in suits]):
        flush = True
    if cards == [chr(ord(cards[0])+i) for i in range(5)]:
        straight = True

    #FLUSH STRAIGHT
    if flush and straight: return (8,cards[-1])
    if flush: return (5,cards[-1])
    if straight: return(4,cards[-1])

    #FOUR OF KIND
    if all([x is cards[0] for x in cards[:4]]):
        return (7,cards[0])
    if all([x is cards[-1] for x in cards[1:]]):
        return (7,cards[-1])

    groups =[]
    groupsize = 1
    for i in range(4):
        if cards[i]!=cards[i+1]:
            groups.append((cards[i],groupsize))
            groupsize=1
        else: groupsize+=1
    groups.append((cards[-1],groupsize))

    if len(groups) == 5: return (0,cards[-1])

    ## full house
    if len(groups) == 2:
        return (6,cards[-1])

    if len(groups)==3:
        #three kind #card[2] garunteed to be in triplet
        if max([x[1] for x in groups]) == 3: return (3,cards[2])

        #two pair
        bestPair = 0
        for g in groups:
            if g[1]==2 and g[0] > bestPair: bestPair = g[0]
        return (2,bestPair)
    #pair
    for g in groups:
            if g[1]==2: return (1,g[0])




p1wins = 0
ties = 0
for hand in allHands:
    #print hand[:15], getRank(hand[:15]), " vs ", getRank(hand[15:]), hand[15:]

    p1score = getRank(hand[:15])
    p2score = getRank(hand[15:])
    if p1score == p2score:
        print "TIE: ", hand[:15], getRank(hand[:15]), " vs ", getRank(hand[15:]), hand[15:]
        ties+=1
    elif p1score > p2score: p1wins+=1

print "player one won:", p1wins
print "unresolved ties:", ties