#피보나치 함수(dp)

def fibonacci(N):
    for i in range(3, N):
        dp[i] = dp[i-1] + dp[i-2]

import sys
T = int(sys.stdin.readline())
for tc in range(1,T+1):
    N = int(sys.stdin.readline())
    dp = [0,1,1] + [0] * (N-2)
    fibonacci(N+1)
    if N == 0:
        print(1, 0)
    elif N==1:
        print(0, 1)
    else:
        print(dp[-2], dp[-1])