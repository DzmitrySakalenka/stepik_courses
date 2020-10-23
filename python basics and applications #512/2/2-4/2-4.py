lines = open("input.txt").readlines()
with open("result.txt", "w") as out:
    out.writelines(reversed(lines))
