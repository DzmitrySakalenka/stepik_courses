def numerics(n):
    return [int(x) for x in list(str(n))]


def kaprekar_step(L):
    sort_L = ''.join([str(x) for x in sorted(L)])
    return int(sort_L[::-1]) - int(sort_L) 


def kaprekar_loop_0(n):
    print(n)
    while(n != 6174):
        n = kaprekar_step(numerics(n))
        print(n)


def kaprekar_loop_1(n):
    if len(set(numerics(n))) == 1:
        print(f'Ошибка! На вход подано число {n} - все цифры одинаковые')
    elif n < 1001:
        print('Ошибка! На вход подано число 1000')
    else:
        print(n)
        while(n != 6174):
            n = kaprekar_step(numerics(n))
            print(n)


def kaprekar_check(n):
    if n in [100, 1000, 100000]:
        return False
    elif len(set(numerics(n))) == 1:
        return False
    elif len(list(numerics(n))) not in [3, 4, 6]:
        return False
    return True


def kaprekar_loop(n):
    if not kaprekar_check(n):
        print(f'Ошибка! На вход подано число {n}, не удовлетворяющее условиям процесса Капрекара')
    else:
        list_nums = [n,]
        print(n)
        while(n not in [495, 6174, 549945, 631764]):
            n = kaprekar_step(numerics(n))
            if n in list_nums:
                print(f'Следующее число - {n}, кажется процесс зациклился...')
                break
            else:
                list_nums.append(n)
                print(n)