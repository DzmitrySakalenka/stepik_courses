print(input())

print(*[input() for _ in range(2)], sep='$')

B1 = 'qwertyuiop'
B2 = B1[1::2]

C1 = 'qwertyuiop'
C2 = C1[-2]

L = input()[2:-2].split("', '")
#exec ('L='+input())