s = input()
countGC = s.count('c') + s.count('g') + s.count('C') + s.count('G')
countS = len(s)
print(float(countGC/countS*100))


s = input()

ind = 0
ch = s[0]

sp = str('')

for i in s:
    if (ch != i):
        sp = sp + ch + str(ind)
        ind = 1
        ch = i
    else:
        ind = ind + 1

sp = sp + ch + str(ind)
      
print(sp)
