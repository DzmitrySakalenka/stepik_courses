a = int(input())
b = int(input())
c = int(input())
d = int(input())

print(' ', end='\t')
for j in range(c, d+1):
    print(j, end='\t')
print()
for i in range(a, b+1):
    print(i, end='\t')
    for j in range(c, d+1):
        print(i*j, end='\t')
    print()


s = 0
k = 0

a = int(input())
b = int(input())

while True:
    if(a%3 != 0):
        a = a + 1
    else:
        break

for i in range(a, b+1, 3):
    k = k + 1
    s = s + i
    
print(float(s/k))