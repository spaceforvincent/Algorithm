#N과 M 11

from itertools import product
import sys

N, M = map(int, sys.stdin.readline().split())
data = sorted(list(map(int, input().split())))
for i in sorted(set(product(data, repeat = M))):
    print(*i)
