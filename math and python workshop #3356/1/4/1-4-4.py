def counter(T):
    c = 0
    l = 0
    
    for i in T:
        if len(set(i.lower())) > c:
            l = len(i)
            c = len(set(i.lower()))
        elif (len(set(i.lower())) == c) & (len(i) > l):
            l = len(i)
            c = len(set(i.lower()))
    return l