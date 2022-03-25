#N과 M 5
#순열
from itertools import permutations
import sys

N, M = map(int, sys.stdin.readline().split())
data = list(map(int, input().split()))
for i in sorted(permutations(data, M)):
    print(*i)