n = int(input())
dictionary = [input().lower() for i in range(n)]

n = int(input())
words = []
for i in range(n):
  str = input().split(' ')
  for word in str:
    words.append(word)

d = {*[elem for elem in words if dictionary.count(elem.lower()) == 0]}

print(*d, sep='\n')