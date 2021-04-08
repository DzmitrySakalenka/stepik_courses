n = int(input())
a = 1
an = 0

while n != 0:
    if an < a:
        print(a, end=' ')
        an += 1
    else:
        a += 1
        print(a, end=' ')
        an = 1
    n -= 1