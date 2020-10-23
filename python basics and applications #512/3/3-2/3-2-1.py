s, a, b = (input() for _ in range(3))

def repl_gen(s, a, b):
    while a in s: s = s.replace(a, b); yield True

print('Impossible' if a in b and a in s else sum(repl_gen(s, a, b)))