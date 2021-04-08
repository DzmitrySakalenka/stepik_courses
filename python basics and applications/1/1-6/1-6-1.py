def is_parent(child, parent):
    return child == parent or any(map(lambda p: is_parent(p, parent), parents[child]))


parents = {}

for _ in range(int(input())):
    a = input().split()
    parents[a[0]] = [] if len(a) == 1 else a[2:]

for _ in range(int(input())):
    a, b = input().split()
    print("Yes" if is_parent(b, a) else "No")