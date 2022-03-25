#N과 M
#순열
from itertools import permutations
import sys

N, M = map(int, sys.stdin.readline().split())
data = list(range(1,N+1))
for i in permutations(data, M):
    print(*i)