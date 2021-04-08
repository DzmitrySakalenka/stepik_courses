steps = {"север": 0, "восток": 0, "запад": 0, "юг": 0}

n = int(input())
for i in range(n):
    step = input().split()
    steps[step[0]] += int(step[1])

print("{0} {1}".format(steps["восток"] - steps["запад"], steps["север"] - steps["юг"]))