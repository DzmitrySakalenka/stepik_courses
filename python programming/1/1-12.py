a = float(input())
b = float(input())
c = float(input())

p = (a+b+c)/2

s = (p*(p-a)*(p-b)*(p-c))**0.5

print(s)


a = int(input())

if (a > -15 and a <= 12) or (a > 14 and a < 17) or (a >= 19):
    print('True')
else:
    print('False')


a = float(input())
b = float(input())
c = input()

if ((c == '/') or (c == 'mod') or (c == 'div')) and (b == 0):
    print('Деление на 0!')
else:
    if (c == '+'):
        print(a+b)
    elif (c == '-'):
        print(a-b)
    elif (c == '/'):
        print(a/b)
    elif (c == '*'):
        print(a*b)
    elif (c == 'mod'):
        print(a%b)
    elif (c == 'pow'):
        print(a**b)
    else:
        print(a//b)


q = input()

if (q == 'треугольник'):
    a = float(input())
    b = float(input())
    c = float(input())
    p = (a+b+c)/2
    print((p*(p-a)*(p-b)*(p-c))**0.5)
elif (q == 'прямоугольник'):
    a = float(input())
    b = float(input())
    print(a*b)
elif (q == 'круг'):
    a = float(input())
    print(3.14*(a**2))


a = int(input())
b = int(input())
c = int(input())

if (a >= b and a >= c):
    print(a)
    if(b <= c):
        print(b)
        print(c)
    else:
        print(c)
        print(b)
elif (b >= a and b >= c):
    print(b)
    if(a <= c):
        print(a)
        print(c)
    else:
        print(c)
        print(a)
else:
    print(c)
    if(a <= b):
        print(a)
        print(b)
    else:
        print(b)
        print(a)


a = int(input())

k = a%10
q = (a%100)//10

if(q == 1):
    print(str(a) + ' программистов')
else:
    if(k == 0 or k >=5):
        print(str(a) + ' программистов')
    elif(k > 1 and k < 5):
        print(str(a) + ' программиста')
    else:
        print(str(a) + ' программист')


c = int(input())

a = c%1000
b = c//1000

a1 = a%10
a2 = (a//10)%10
a3 = a//100

b1 = b%10
b2 = (b//10)%10
b3 = b//100

if((a1+a2+a3) == (b1+b2+b3)):
    print('Счастливый')
else:
    print('Обычный')