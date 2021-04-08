import math


a = int(input())
b = int(input())
c = int(input())

p = a + b + c

print(p)
print(math.sqrt(p/2 * (p/2 - a) * (p/2 - b) * (p/2 - c)))