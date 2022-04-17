#피보나치 수(dp)


def fibonacci(N):
    for i in range(3, N):
        dp[i] = dp[i-1] + dp[i-2]

import sys
N = int(sys.stdin.readline())
dp = [0,1,1] + [0] * (N-2)
fibonacci(N+1)
print(dp[-1])