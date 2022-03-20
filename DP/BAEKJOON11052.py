#카드 구매하기

import sys
N = int(sys.stdin.readline())
card_pack = [0] + list(map(int, sys.stdin.readline().split()))
dp = [0] * (N+1)

for i in range(1,N+1):
    for k in range(1,i+1):
        dp[i] = max(dp[i], dp[i-k] + card_pack[k])

print(dp[i])