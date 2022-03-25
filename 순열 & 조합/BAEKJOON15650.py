#N과 M2
#조합
from itertools import combinations
import sys

N, M = map(int, sys.stdin.readline().split())
data = list(range(1,N+1))
for i in combinations(data, M):
    print(*i)