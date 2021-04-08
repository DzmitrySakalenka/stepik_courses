def f(x):
    if x <= -2:
        return (1-(x+2)**2)
    elif x <= 2 and x >- 2:
        return -(x/2)
    elif x > 2:
        return (x-2)**2 + 1


def modify_list(l):
    l_new = []
    for k in l:
        if k % 2 == 0:
            l_new.append(int(k//2))
    l.clear()
    for i in l_new:
        l.append(i)