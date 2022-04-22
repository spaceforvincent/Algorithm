#좌표 정렬하기2

import sys
T = int(sys.stdin.readline())

lst = []
for i in range(1,T+1):
    x1, x2 = map(int, sys.stdin.readline().split())
    lst.append((x1,x2))



for a in sorted(lst, key=lambda x:(x[1],x[0])):
    print(*a)