#y больше или равно x
#y делится нацело на 5
import math

def closest_mod_5(x):
    return math.ceil(x / 5) * 5

print(closest_mod_5(3),closest_mod_5(13),closest_mod_5(10))