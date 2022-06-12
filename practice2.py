#소수 찾기
import sys
N = int(sys.stdin.readline())

lst = list(map(int, sys.stdin.readline().split()))
sosu_cnt = 0
for i in lst:
    cnt = 0
    if i == 1:
        continue

    for j in range(2, i+1):
        if (i % j == 0):
            cnt += 1
    if cnt == 1:
        sosu_cnt += 1

print(sosu_cnt)