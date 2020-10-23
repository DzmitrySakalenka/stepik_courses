ROMANS = (('M',  1000),
          ('CM', 900),
          ('D',  500),
          ('CD', 400),
          ('C',  100),
          ('XC', 90),
          ('L',  50),
          ('XL', 40),
          ('X',  10),
          ('IX', 9),
          ('V',  5),
          ('IV', 4),
          ('I',  1))


def rome_numerals(data):
    num = ''
    for roman, value in ROMANS:
        while data >= value:
            data -= value
            num += roman
    return num

print(rome_numerals(int(input())))


a = int(input())
print('Division by zero!' if a == 0 else round(int(input()) / a, 1))


tt = input()

if tt == 'int':
    a = int(input())
    b = int(input())
    if a == 0 and b == 0:
        print('Empty Ints')
    else:
        print(a+b)
elif tt == 'str':
    a = input()
    if a:
        print(a)
    else:
        print('Empty String')
    #(lambda a: print(a) if a else print('Empty String'))(input())
elif tt == 'list':
    a = input().split()
    if a:
        print(a[-1])
    else:
        print('Empty List')
else:
    print('Unknown type')
