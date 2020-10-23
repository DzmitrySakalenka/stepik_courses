[print(i) for i in range(int(input())+1)]

[print(n**2) for n in range(0, int(input()), 2)]

s = 0
while(True):
    a = input()
    if a == 'The End':
        print(s)
        break
    s += int(a)
# or print(sum(map(int, iter(input, 'The End'))))


for word in input().split():
    if word[0] != '*': print(word)
#or [print(s) for s in input().split() if not s.startswith('*')]

a = int(input())
for i in range(2, a):
    if a % i == 0:
        print(i)
        break

[print(n**3) for n in range(1, abs(int(input())))]