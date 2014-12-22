def letToCode(ch): return ord(ch) - ord('A')+1
def WordCode(w):
    return sum(map(letToCode,list(w)))

print WordCode("SKY")

f = open("words.txt")
words = f.read()
words = words.translate(None, '"')
words = words.split(",")

words = map(WordCode, words)

print words[:40]

highscore = max(words)

triagNums =[]
tnumber = 1
nth = 1
while tnumber<=highscore:
    triagNums.append(tnumber)
    nth +=1
    tnumber+=nth

print highscore
print triagNums

triWords = filter(lambda x:x in triagNums, words)
#triWords = [x for x in words if x in triagNums]
print len(triWords)