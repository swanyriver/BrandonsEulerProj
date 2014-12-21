
concat = []

for thous in range(10):
    for hund in range(10):
        for tens in range(10):
            for ones in range(10):
                newNum = [thous,hund,tens,ones]
                while newNum and not newNum[0]: del newNum[0]
                concat.extend(newNum)

#print concat[:100]
#print concat[-45:]
concat.insert(0, 0)
print concat[10]
print concat[100]
print concat[1000]
print concat[10000]
print concat[9997:10003]