s = input()
t = input()

print(sum(1 for i in range(len(s)) if s.startswith(t, i)))