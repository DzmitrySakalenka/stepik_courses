print(sum(map(int, input().split())))

print(*[sum(map(int, input().split())) for _ in (1,2)], sep="#")

print(*set(input().split('&')))

(lambda s : print(s[1], s[2], s[-2],sep=' '))(input().split())

print(*input().split()[::-1], sep="-$-")

(lambda s: print(len(s), s.count('one')))(input().split())

print(sum(map(int, input().split())))