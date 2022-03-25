#N과 M 8
#중복조합
from itertools import combinations_with_replacement
import sys

N, M = map(int, sys.stdin.readline().split())
data = sorted(list(map(int, input().split())))
for i in sorted(combinations_with_replacement(data, r = M)):
    print(*i)