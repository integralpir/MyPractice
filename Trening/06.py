# 0 1 2 3 4 5
import sys

def get(n):
    if n == 0:
        return 0
    else:
        return get(n-1+n)

sys.setrecursionlimits(1600)
n = int(input())
print(get())
