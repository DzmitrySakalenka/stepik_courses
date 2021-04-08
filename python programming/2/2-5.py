a = [int(i) for i in input().split()]
asum = sum(list(a))
print(asum)


a = [int(i) for i in input().split()]
i = len(a)

if i == 1:
    print(a[0])
else:  
    b = [0 for i in range(i)]
    for k in range(i):
        l = k - 1
        r = k + 1
        if l == -1:
            l = i - 1
        if r == i:
            r = 0
        b[k] = a[l] + a[r]
        print(b[k], end=' ')


a = [int(i) for i in input().split()]
i = len(a)
a.sort()
if i > 1:
    ch = a[0]
    if ch == a[1]:
        print(ch, end=' ')
    for k in range(i-2):
        if a[k+1] != ch:
            ch = a[k+1]
            if a[k+1] == a[k+2]:
                print(ch, end=' ')