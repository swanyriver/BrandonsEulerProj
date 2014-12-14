file=open("triangle.txt") # Generates a list. Each element of the list is a list containing the elements of a row of the triangle.
t=file.read()
t=t.split("\n")
for i in range(len(t)):
    t[i]=t[i].split()

del(t[len(t)-1])
print t

for i in range(len(t)): # Converts all elements in the list to int.
    print i
    for j in range(i+1):
        t[i][j]=int(t[i][j])

pyra = t
gpath =[]
gpath.append(pyra[0])


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