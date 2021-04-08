def kaprekar_10(n):
    divider = 10
    while True:
        left, right = divmod(n**2, divider)
        
        if left == 0:
            return False
        
        if right != 0 and left + right == n:
            return True
        
        divider *= 10


def convert(num, to_base=10, from_base=10):
    alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dec = int(str(num), from_base)
    ans = ''

    if dec == 0:
        return '0'

    while dec > 0:
        ans = alpha[dec % to_base] + ans
        dec = dec // to_base
    
    return ans


def kaprekar(n, base=10):
    n = int(str(n), base=base)

    str_square = convert(n**2, base)
    for i in range(1, len(str_square)):
        a, b = int(convert(str_square[:i], from_base=base)), int(convert(str_square[i:], from_base=base))
        if a * b and a + b == n :
            return True

    return False



test_1 = [9, 45, 55, '99', '297', 703, 999, '2223', 2728, '4879']
test_2 = [10, 46, 56, 100, 298, 704, '1000', '2224', '2729', '4880']
test_3 = ['6', 'A', 'F', '33', '55', '5B', '78', '88', 'AB', 'CD', 'FF', '15F', '334', '38E']

print([kaprekar(i) for i in test_1]) # Тест чисел Капрекара из системы с основанием 10

print([kaprekar(i) for i in test_2 ]) # Тест НЕ чисел Капрекара из системы с основанием 10

print([kaprekar(i, base=16) for i in test_3]) #Тест чисел Капрекара из системы с основанием 16
