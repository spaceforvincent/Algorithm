#날짜 계산

import sys
target = list(map(int, sys.stdin.readline().split()))

#1<=E<=15 1<=S<=28 1<=M<=19
# 1 1 1이 E S M이랑 같아질때까지 각자 범위 돌면서 계속 커진다...

ans = 1
lst = [1,1,1]
while lst != target:
    ans += 1
    lst[0] += 1
    lst[1] += 1
    lst[2] += 1

    if lst[0] > 15:
        lst[0] = 1
    if lst[1] > 28:
        lst[1] = 1
    if lst[2] > 19:
        lst[2] = 1

print(ans)
    
    