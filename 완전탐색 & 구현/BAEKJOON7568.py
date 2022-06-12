#덩치

import sys

N = int(sys.stdin.readline())

lst = []
for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    lst.append((x,y))

for i in lst:
    rank = 1
    for j in lst:
        if i[0] < j[0] and i[1] < j[1]: #더 덩치큰 사람이 있다면
            rank += 1 #뒤로 밀려남
    print(rank, end = " ")