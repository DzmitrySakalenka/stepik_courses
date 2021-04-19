countObjects, countVarinCallers = map(int, input().split())

if countVarinCallers <= 2:
    ans = 2 + countObjects + countObjects * countVarinCallers
else:
    ans = 2 + countObjects + countObjects * countVarinCallers + countObjects * countVarinCallers* (countVarinCallers-1) // 2

print(ans)