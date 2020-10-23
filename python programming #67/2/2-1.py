i = 1
s = 0
while(i != 0):
  i = int(input())
  s = s + i
print(s)


a = int(input())
b = int(input())

if(a > b):
  c = a
else:
  c = b
  
while(c%a != 0 or c%b != 0):
  c = c + 1

print(c)