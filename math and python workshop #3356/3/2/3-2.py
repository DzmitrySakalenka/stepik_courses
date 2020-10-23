from math import atan, exp


def f(x):
    return 2 * atan(x)

lim = f(float('+inf'))
print (lim)


def def_e(x, dx=0.00001):
    return (exp(x + dx) - exp(x)) / dx


def even_indeces(L):
    return L[0::2]


def even_elements(l):
    return [i for i in l if i % 2 == 0]


def last_to_first(l):
    return l[::-1]


print(sum(list(i for i in range(int(input())+1) if i % 3 != 0 and i % 5 == 0)))


def common(list_a, list_b):
    return list(set(list_a) & set(list_b))


def front_x(words):
    return sorted(words, key=lambda x: (x[:1] != 'x', x))


def fib(n):
    x_1 = 0
    x_2 = 1
    for _ in range(n-1):
        x_2, x_1 = x_2+x_1, x_2
    return x_2
#or
#def fib(n):
#    return fib(n-1)+fib(n-2) if n>2 else 1
#or (f Binne)
#def fib(q: int) -> int:
#    return pow(2 << q, q + 1, (4 << 2 * q) - (2 << q) - 1) % (2 << q)


def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def donuts(n):
    return n if n < 10 else 'много'


n = int(input())
print(f'Всего пончиков: {donuts(n)}')


def both_ends(s):
    return s[:2]+s[-2:] if len(s) > 1 else ''


def fix_start(s):
    return s[0]+s[1:].replace(s[0], '*')

