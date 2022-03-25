#N과 M 7
#중복순열
from itertools import product
import sys

N, M = map(int, sys.stdin.readline().split())
data = sorted(list(map(int, input().split())))
for i in sorted(product(data, repeat = M)):
    print(*i)