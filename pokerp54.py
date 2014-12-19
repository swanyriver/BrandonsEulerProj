from string import maketrans
fileName = "testpoker.txt"

pfile = open(fileName)

allHands = pfile.read()

outtab = ""
for i in range(1,6): outtab+=chr(ord('9')+i)
transtab = maketrans("TJQKA",outtab)
allHands = allHands.translate(transtab)

allHands = allHands.split('\n')


def getRank(hand):
    flush,straight,Four,Three,Pair,FullHouse = False,False,False,False,False,False

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
        return (7,cards[-1])
    if all([x is cards[-1] for x in cards[1:]]):
        return (7,cards[0])





print "hello"
#print getRank("7D 7S 7C ;C 7C")
#print getRank("7D 7C 7C 4C 7C")
#print getRank("7D 8C 7C 4C 7C")
#print getRank("5D 4C 6C 8C 7C")
print getRank("5D 5C 8C 9C 8C")
print getRank("1D 3C 2C 9C 9C")
print getRank("5D 5C 8C 8C 8C")
print getRank("1D 5C 5C 5C 8C")