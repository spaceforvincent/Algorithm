#N과 M 6
#조합
from itertools import combinations
import sys

N, M = map(int, sys.stdin.readline().split())
data = sorted(list(map(int, input().split())))
for i in sorted(combinations(data, M)):
    print(*i)