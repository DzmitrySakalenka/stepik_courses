def update_dictionary(d, key, value):
    if d.get(key) != None:
        d[key].append(value)
    elif d.get(key*2) != None:
        d[key*2].append(value)
    else:
        d[key*2] = [value]


words = input().lower().split(" ")
word={}

for i in words:
    if word.get(i) != None:
        word[i] = word[i] + 1
    else:
        word.setdefault(i, 1)

for key, value in word.items():
    print(key, value)


n = int(input())
dic = {}

for n in range(0, n):
    n = int(input())
    if dic.get(n) == None:
        dic.setdefault(n, f(n))
    print(dic[n])