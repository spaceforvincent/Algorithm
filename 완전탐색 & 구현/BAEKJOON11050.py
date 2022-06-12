#이항계수 1
import sys

N, K = map(int, sys.stdin.readline().split())

a = 1
for k in range(K):
    a *= N-k

for k in range(K,0,-1):
    a/=k

print(int(a))
