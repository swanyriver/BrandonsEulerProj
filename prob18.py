
pyra = []
pyra.append([75])
pyra.append([95,64])
pyra.append([17,47,82])
pyra.append([18,35,87,10])
pyra.append([20, 4,82,47,65])
pyra.append([19, 1,23,75, 3,34])
pyra.append([88, 2,77,73, 7,63,67])
pyra.append([99,65, 4,28, 6,16,70,92])
pyra.append([41,41,26,56,83,40,80,70,33])
pyra.append([41,48,72,33,47,32,37,16,94,29])
pyra.append([53,71,44,65,25,43,91,52,97,51,14])
pyra.append([70,11,33,28,77,73,17,78,39,68,17,57])
pyra.append([91,71,52,38,17,14,91,43,58,50,27,29,48])
pyra.append([63,66, 4,68,89,53,67,30,73,16,69,87,40,31])
pyra.append([04,62,98,27,23, 9,70,98,73,93,38,53,60, 4,23])

gpath =[]
gpath.append([75])

for row in range(len(pyra)-1):
#for row in range(5):
    gpath.append([0] * (row+2))
    for c in range(row+1):
        suma = gpath[row][c]+pyra[row+1][c]
        gpath[row+1][c] = max( gpath[row+1][c],suma)

        sumb = gpath[row][c]+pyra[row+1][c+1]
        gpath[row+1][c+1] = max( gpath[row+1][c+1],sumb)

#for row in gpath:
#    print row

print max(gpath[len(gpath)-1])