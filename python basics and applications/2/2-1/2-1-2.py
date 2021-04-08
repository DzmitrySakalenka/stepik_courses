def is_parent(child, parent):
    return child == parent or any(map(lambda p: is_parent(p, parent), parents[child]))


parents = {}

for _ in range(int(input())):
    a = input().split()
    parents[a[0]] = [] if len(a) == 1 else a[2:]
    
excepts = []

for _ in range(int(input())):
    excpt = input()
    
    for k in excepts:
        if is_parent(excpt, k):
            print(excpt)
            break
    
    excepts.append(excpt)


