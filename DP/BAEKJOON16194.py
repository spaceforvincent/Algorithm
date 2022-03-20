#카드 구매하기2

import sys
N = int(int(sys.stdin.readline()))
card_pack = [0] + list(map(int, sys.stdin.readline().split()))
dp = [0]*(N+1)
 
for i in range(1,N+1):
    min_val = 987654321
    for k in range(1,i+1):
        min_val = min(min_val, dp[i-k] + card_pack[k])
    dp[i] = min_val

print(dp[N])
