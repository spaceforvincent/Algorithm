#수 찾기

import sys


N = int(sys.stdin.readline())
A = sorted(list(map(int, input().split())))
M = int(sys.stdin.readline())
B = list(map(int, input().split()))

ans = []
for i in range(M):
    l = 0
    r = N-1
    while l<=r:
        m = (l + r)//2
        if A[m] == B[i]:
            ans.append(1)
            break
        elif A[m] < B[i]:
            l = m + 1
        elif A[m] > B[i]:
            r = m - 1
    else:
        ans.append(0)

for i in ans:
    print(i)