def factorial(n):
    f = 1

    while n > 1:
        f *= n
        n -= 1
    
    return f


n, k = map(int, input().split())

print(int(factorial(n) / (factorial(k)*factorial(n-k))))