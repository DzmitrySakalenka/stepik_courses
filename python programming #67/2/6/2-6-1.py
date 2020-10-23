sum = int(input())
quad = sum*sum

while sum != 0:
    a = int(input())
    sum += a
    quad += a*a 

print(quad)