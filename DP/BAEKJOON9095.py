#1,2,3 더하기
import sys
N = int(sys.stdin.readline())

dp = [0, 1, 2, 4]
for i in range(4, 12):
    dp.append(dp[i-3]+dp[i-2]+dp[i-1])
for i in range(N):
    print(dp[int(sys.stdin.readline())])