#N과 M4
#중복조합
from itertools import combinations_with_replacement
import sys

N, M = map(int, sys.stdin.readline().split())
data = list(range(1,N+1))
for i in combinations_with_replacement(data, r=M):
    print(*i)