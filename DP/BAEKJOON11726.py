#2xn 타일링

import sys
N = int(sys.stdin.readline())

dp = [1] + [0] * N

dp[1] = 1

for i in range(2,N+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[N]%10007)