import math
import functools


def zero(n):
    return functools.reduce(lambda r, i: r + math.floor(n/(5**i)), range(0, len(str(n))+2))

print(zero(1000))
