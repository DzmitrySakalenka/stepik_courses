import math


a = int(input())

ss = a**2*math.sqrt(3)/4
a *= 3
sb = a**2*math.sqrt(3)/4

print(round(sb + 2*ss))