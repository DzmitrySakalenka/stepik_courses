lst = [int(i) for i in input().split()]
x = int(input())
i = len(lst)
l = False

for k in range(i):
    if lst[k] == x:
        print(k, end=' ')
        l =True

if l == False:
    print('Отсутствует')