import math


for i in range(len(L)-1):
    if math.fabs(L[i]-L[i+1]) == 1:
        index = i
        break