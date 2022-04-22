#좌표 정렬하기

import sys
T = int(sys.stdin.readline())

lst = []
for i in range(1,T+1):
    x1, x2 = map(int, sys.stdin.readline().split())
    lst.append((x1,x2))

for a in sorted(lst):
    print(*a)