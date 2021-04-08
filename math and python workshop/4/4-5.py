from itertools import product


simple_multiplication = lambda x, y: (100-((100-x)+(100-y)))*100+(100-x)*(100-y)
simple_multiplication_check = lambda x, y: (simple_multiplication(x, y) - x*y) == 0
multiplication_check = lambda x, y, length_check: (wisdom_multiplication(x, y, length_check) - x*y) == 0


def multiplication_check_list(start=10, stop=99, length_check = True):
    a, b =0, 0

    for i, j in product(range(start, stop+1), range(start, stop+1)):
        if multiplication_check(i, j, length_check):
            a += 1
        else:
            b += 1

    print(f'Правильных результатов: {a}\nНеправильных результатов: {b}')


def wisdom_multiplication(x, y, length_check=True):
    s1 = str(100-(100-x)-(100-y))
    s2 = str((100-x)*(100-y))
    return int(s1+'0'+s2 if length_check and len(s2)==1 else s1+s2)


multiplication_check_list(98, 99, length_check = False)
