#N과 M 12

from itertools import combinations_with_replacement
import sys

N, M = map(int, sys.stdin.readline().split())
data = sorted(list(map(int, input().split())))
for i in sorted(set(combinations_with_replacement(data, r = M))):
    print(*i)
