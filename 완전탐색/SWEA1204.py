#최빈수 구하기

import sys
sys.stdin = open('swea1204_input.txt')

T= int(input())
for tc in range(1,T+1):
    tc = int(input())
    arr = list(map(int, input().split()))

    cnt = [0] * 1000
    for score in arr:
        cnt[score] += 1
    
    max_v = 0
    max_i = 0
    for i in range(len(cnt)):
        if max_v <= cnt[i]:
            max_v = cnt[i]
            max_i = i

    print(f'#{tc} {max_i}')

