import itertools


n = int(input())
x_list = [input().split(';') for x in range(n)]
vs = [(x[0], x[2]) for x in x_list]

clubs = set(itertools.chain.from_iterable(vs))
res = {club:[0, 0, 0, 0, 0] for club in clubs}

for club1, points1, club2, points2 in x_list:
    res[club1][0] += 1
    res[club2][0] += 1
    if int(points1) > int(points2):
        res[club1][1] += 1
        res[club1][4] += 3
        res[club2][3] += 1
    elif int(points1) < int(points2):
        res[club2][1] += 1
        res[club2][4] += 3
        res[club1][3] += 1
    elif int(points1) == int(points2):
        res[club1][2] += 1
        res[club1][4] += 1
        res[club2][2] += 1
        res[club2][4] += 1

for club in clubs:
    print('{}:{}'.format(club, ' '.join(map(str, res[club]))))