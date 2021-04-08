from math import sin, pi
from random import choice


def f1(x):
    return (2*x**2 - 3*x - 5) / (3*x**2 + x + 1)


def f2(x):
    return (sin(pi*x/2))/x


def derivative_v1(f, x0=0):
    return round((f(x0+(1e-7))-f(x0))/(1e-7), 3)


def list_pull(L):
    res = []
    for elem in L:
        res += list_pull(elem) if isinstance(elem, list) else [elem]
    return res


def list_copy(L1):
    res = []
    for elem in L1:
        res.append(list_copy(elem) if isinstance(elem, list) else elem) 
    return res


def mimic_dict_v1(string):
    words = string.split()
    d = {'': [words[0]]}

    for i in range(len(words)-1):
        if d.get(words[i]) is None:
            d[words[i]] = []
        d[words[i]].append(words[i+1])
    
    return d


def mimic_dict_v2(string):
    words = string.split()
    d = {}
    prev_word = ""

    for word in words:
        d.setdefault(prev_word, []).append(word)
        prev_word = word

    return d


def print_mimic(mdict, word, n=200):
    answer = []
    for _ in range(n):
        answer.append(word)
        word = choice(mdict.get(word, mdict['']))
    return ' '.join(answer)


derivative_v2 = lambda f, x0=0: round((f(x0+1e-7)-f(x0))/(1e-7),3)

verbing = lambda s: s if len(s) < 3 else s + ('ing','ly')['ing' in s]

front_back = lambda a,b: a[:-(len(a)//2)] + b[:-(len(b)//2)] + a[-(len(a)//2):] + b[-(len(b)//2):]


print(round(f1(1e7), 3))
print(round(f1(-1e7), 3))
print(*list(map(lambda x: round((2*x*x-3*x-5)/(3*x*x+x+1),3),[1e7,-1e7])),sep='\n')

print(round(f2(1e7), 3))
print((lambda x: round(sin(pi*x/2)/x,3))(1e7))

print(derivative_v1(sin))
print(derivative_v2(sin))

print(list_pull([['one'], [343, 2], [[9, 9, 9], [[666, 666], [[[[42]]]]]]]))

L1 = [['one'], [343, 2], [[9, 9, 9], [[666, 666], [[[[42]]]]]]]
L2 = list_copy(L1)

print(L1, L2)
L1[2][1][1][0][0][0][0] = 'z'
print(L1, L2)

print(verbing('hail'))
print(verbing('swiming'))
print(verbing('do'))

print(front_back('abcd', 'xy'))
print(front_back('abcde', 'xyz'))
print(front_back('Kitten', 'Donut'))

print(mimic_dict_v1('Uno dos tres cuatro cinco'))
print(mimic_dict_v1('a cat and a dog\na fly'))
print(mimic_dict_v2('Uno dos tres cuatro cinco'))
print(mimic_dict_v2('a cat and a dog\na fly'))

mimic_dict = mimic_dict_v1('We are not what we should be\nWe are not what we need to be\nBut at least we are not what we used to be\n  -- Football Coach')
print(print_mimic(mimic_dict, ''))
