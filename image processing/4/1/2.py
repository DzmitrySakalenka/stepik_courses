from math import pi, e


array = list(map(int, input().split()))
sigma = array[0]
x = array[1]
y = array[2]
result = 1/((2*pi)*sigma**2)*e**((-x**2 - y**2)/(2*sigma**2))
print(result)