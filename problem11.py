
grid = []
grid.append([8,2,22,97,38,15,0,40,0,75,4,5,7,78,52,12,50,77,91,8])
grid.append([49,49,99,40,17,81,18,57,60,87,17,40,98,43,69,48,4,56,62,0])
grid.append([81,49,31,73,55,79,14,29,93,71,40,67,53,88,30,3,49,13,36,65])
grid.append([52,70,95,23,4,60,11,42,69,24,68,56,1,32,56,71,37,2,36,91])
grid.append([22,31,16,71,51,67,63,89,41,92,36,54,22,40,40,28,66,33,13,80])
grid.append([24,47,32,60,99,3,45,2,44,75,33,53,78,36,84,20,35,17,12,50])
grid.append([32,98,81,28,64,23,67,10,26,38,40,67,59,54,70,66,18,38,64,70])
grid.append([67,26,20,68,2,62,12,20,95,63,94,39,63,8,40,91,66,49,94,21])
grid.append([24,55,58,5,66,73,99,26,97,17,78,78,96,83,14,88,34,89,63,72])
grid.append([21,36,23,9,75,0,76,44,20,45,35,14,0,61,33,97,34,31,33,95])
grid.append([78,17,53,28,22,75,31,67,15,94,3,80,4,62,16,14,9,53,56,92])
grid.append([16,39,5,42,96,35,31,47,55,58,88,24,0,17,54,24,36,29,85,57])
grid.append([86,56,0,48,35,71,89,7,5,44,44,37,44,60,21,58,51,54,17,58])
grid.append([19,80,81,68,5,94,47,69,28,73,92,13,86,52,17,77,4,89,55,40])
grid.append([4,52,8,83,97,35,99,16,7,97,57,32,16,26,26,79,33,27,98,66])
grid.append([88,36,68,87,57,62,20,72,3,46,33,67,46,55,12,32,63,93,53,69])
grid.append([4,42,16,73,38,25,39,11,24,94,72,18,8,46,29,32,40,62,76,36])
grid.append([20,69,36,41,72,30,23,88,34,62,99,69,82,67,59,85,74,4,36,16])
grid.append([20,73,35,29,78,31,90,1,74,31,49,71,48,86,81,16,23,57,5,54])
grid.append([1,70,54,71,83,51,54,69,16,92,33,48,61,43,52,1,89,19,67,48])

gridb =[]
gridb.append([ 8, 2,22,97,38,15, 0,40, 0,75, 4, 5, 7,78,52,12,50,77,91, 8])
gridb.append([49,49,99,40,17,81,18,57,60,87,17,40,98,43,69,48, 4,56,62, 0])
gridb.append([81,49,31,73,55,79,14,29,93,71,40,67,53,88,30, 3,49,13,36,65])
gridb.append([52,70,95,23, 4,60,11,42,69,24,68,56, 1,32,56,71,37, 2,36,91])
gridb.append([22,31,16,71,51,67,63,89,41,92,36,54,22,40,40,28,66,33,13,80])
gridb.append([24,47,32,60,99, 3,45, 2,44,75,33,53,78,36,84,20,35,17,12,50])
gridb.append([32,98,81,28,64,23,67,10,26,38,40,67,59,54,70,66,18,38,64,70])
gridb.append([67,26,20,68, 2,62,12,20,95,63,94,39,63, 8,40,91,66,49,94,21])
gridb.append([24,55,58, 5,66,73,99,26,97,17,78,78,96,83,14,88,34,89,63,72])
gridb.append([21,36,23, 9,75, 0,76,44,20,45,35,14, 0,61,33,97,34,31,33,95])
gridb.append([78,17,53,28,22,75,31,67,15,94, 3,80, 4,62,16,14, 9,53,56,92])
gridb.append([16,39, 5,42,96,35,31,47,55,58,88,24, 0,17,54,24,36,29,85,57])
gridb.append([86,56, 0,48,35,71,89, 7, 5,44,44,37,44,60,21,58,51,54,17,58])
gridb.append([19,80,81,68, 5,94,47,69,28,73,92,13,86,52,17,77, 4,89,55,40])
gridb.append([ 4,52, 8,83,97,35,99,16, 7,97,57,32,16,26,26,79,33,27,98,66])
gridb.append([88,36,68,87,57,62,20,72, 3,46,33,67,46,55,12,32,63,93,53,69])
gridb.append([ 4,42,16,73,38,25,39,11,24,94,72,18, 8,46,29,32,40,62,76,36])
gridb.append([20,69,36,41,72,30,23,88,34,62,99,69,82,67,59,85,74, 4,36,16])
gridb.append([20,73,35,29,78,31,90, 1,74,31,49,71,48,86,81,16,23,57, 5,54])
gridb.append([ 1,70,54,71,83,51,54,69,16,92,33,48,61,43,52, 1,89,19,67,48])


largest = 0
gridsize=len(grid)

def rowcheck(lgrid):
    largest = 0
    for row in lgrid:
        for pos in range(4,len(row)+1):
            product = 1
            for f in row[pos-4:pos]:
                product*= f
            if product > largest:
                largest = product
            print row[pos-4:pos], product
        print "######################################"

    return largest


#Rows
rowproduct = 0
rowproduct = rowcheck(grid)
if rowproduct > largest:
    largest = rowproduct

#collumn
gridcol = []
for c in range(gridsize):
    col = []
    for r in range(gridsize):
        col.append(grid[r][c])
    gridcol.append(col)

rowproduct = rowcheck(gridcol)
if rowproduct > largest:
    largest = rowproduct


#diag   tl to br
diagl = []
for x in range(gridsize-3):
    r=0
    row = []
    for c in range(x,gridsize):
        row.append(grid[r][c])
        r+=1
    diagl.append(row)

for x in range(1,gridsize-3):
    c=0
    row = []
    for r in range(x,gridsize):
        row.append(grid[r][c])
        c+=1
    diagl.append(row)

rowproduct = rowcheck(diagl)
if rowproduct > largest:
    largest = rowproduct


#diag tr to br
diagr = []
for x in range(gridsize-3):
    r=gridsize-1
    row = []
    for c in range(x,gridsize):
        row.append(grid[r][c])
        r-=1
    diagr.append(row)

for x in range(gridsize-3):
    r=gridsize-2
    row = []
    for c in range(x,gridsize):
        row.append(grid[r][c])
        r-=1
    diagr.append(row)

rowproduct = rowcheck(diagr)
if rowproduct > largest:
    largest = rowproduct

for row in diagl:
    print row
print "##################"
for row in diagr:
    print row

print largest
