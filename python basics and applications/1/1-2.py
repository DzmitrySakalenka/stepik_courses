objects = [1, 2, 1, 2, 3, True]

print(len(set([id(x) for x in objects])))