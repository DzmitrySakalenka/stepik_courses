l = int(input())

mtx = [[0 for j in range(0, l)] for i in range(0, l)]

def go(ch):
    num = 1
    stroka = 0
    stolbec = l-1
    n=1
    
    while num < l**2 - ch:
        for k in range(0, 2):
            for j in range(stroka, stolbec, n):
                mtx[stroka][j] = num
                num +=1
            
            for i in range(stroka, stolbec, n):
                mtx[i][stolbec] = num
                num +=1
            
            stroka, stolbec = stolbec, stroka
            n = n*(-1)
            k+=1
        stroka +=1
        stolbec -=1

if l%2 == 0:
    go(1)
else:
    go(0)
    mtx[int(l/2)][(int(l/2))] = l**2

for i in range(0, l):
    for j in range(0, l):
        print(mtx[i][j], end=' ')
    print()
