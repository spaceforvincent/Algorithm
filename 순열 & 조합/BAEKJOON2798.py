#블랙잭
from itertools import combinations
import sys

N, M = map(int, sys.stdin.readline().split())
data = map(int, sys.stdin.readline().split())

max_v = 0
for i in combinations(data, 3):
    if sum(i)<=M:
        if max_v < sum(i):
            max_v = sum(i)

print(max_v)