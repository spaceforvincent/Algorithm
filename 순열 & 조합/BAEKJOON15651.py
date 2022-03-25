#N과 M3
#중복순열
from itertools import product
import sys

N, M = map(int, sys.stdin.readline().split())
data = list(range(1,N+1))
for i in product(data, repeat=M):
    print(*i)