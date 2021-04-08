a = int(input())
b = int(input())
h = int(input())

if h < a:
  print('Недосып')
elif h > b:
  print('Пересып')
else:
  print('Это нормально')


a = int(input())

if (a%4 == 0 and a%100 != 0) or (a%400 == 0):
  print('Високосный')
else:
  print('Обычный')