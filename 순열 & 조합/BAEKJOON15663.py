#N과 M 9

from itertools import permutations
import sys

N, M = map(int, sys.stdin.readline().split())
data = sorted(list(map(int, input().split())))
for i in sorted(set(permutations(data, M))):
    print(*i)
