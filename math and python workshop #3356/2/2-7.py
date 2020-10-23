def sum2(a,b):
    return a+b
#or sum2 = lambda a,b: a+b


def Aleksey(name='%UserName%'):
    print(f'Hello, {name}!')


def dfactorial(n):
    return n * dfactorial(n-2) if n > 1 else 1
#or dfactorial = lambda n: int(n<=1) or dfactorial(n-2)*n


def Kfactorial(n,k=1):
    return n * Kfactorial(n-k, k) if n > 1 else 1
#or Kfactorial = lambda n, k=1: (n<1)+0 or Kfactorial(n-k, k)*n


def convert(L):
    return list(map(int, L))
    #or return [int(i) for i in L]
#or convert = lambda L: list(map(int, L))


def translate(a, n=2):
    new_a = ''
    while a>0:
        new_a += str(a%n)
        a //= n
    return new_a[::-1]
#or
#def translate(n, k=2):
#    return n % k if n < k else n % k + translate(n // k, k)*10


factorial = lambda n: int(n<=1) or factorial(n-1)*n
sf = lambda n: int(n<=1) or sf(n-1)*factorial(n)


def maxId(L):
    L = convert(L)
    return L.index(max(L))
#or maxId = lambda L: L.index(max(L, key=int))
#or
#import numpy as np
#def maxId(L):
#    return np.argmax(list(map(int, L)))
