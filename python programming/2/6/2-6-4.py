mtx = []

while True:
    n = str(input())
    if n == 'end':
        break
    mtx.append([int(s) for s in n.split()])

out_mtx = [[0 for j in range(len(mtx[i]))] for i in range(len(mtx))]

for i in range(len(mtx)):
    for j in range(len(mtx[i])):
        ylen = len(mtx)
        xlen = len(mtx[0])
        out_mtx[i][j]=int(mtx[i-1][j]) + int(mtx[(i+1)%ylen][j]) + int(mtx[i][j-1]) + int(mtx[i][(j+1)%xlen])

for i in range(ylen):
    for j in range(xlen):
        print(out_mtx[i][j], end = ' ')
    print()
