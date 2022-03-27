import sys

sys.stdin = open('고대유적_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 행, 열
    field = [0] * N
    for i in range(N):
        arr = list(map(int, input().split()))
        field[i] = arr

    horiz = [0] * N
    for i in range(N):
        cnt = 0
        max_cnt = 0
        for j in range(M):
            if field[i][j] == 1:
                cnt += 1
            else:
                if max_cnt < cnt:
                    max_cnt = cnt
                    cnt = 0
        if max_cnt < cnt:
            max_cnt = cnt
        horiz[i] = max_cnt

    max_horiz = 0
    for i in horiz:
        if max_horiz < i:
            max_horiz = i

    vertic = [0] * M
    for i in range(M):
        cnt = 0
        max_cnt = 0
        for j in range(N):
            if field[j][i] == 1:
                cnt += 1
            else:
                if max_cnt < cnt:
                    max_cnt = cnt
                    cnt = 0
        if max_cnt < cnt:
            max_cnt = cnt
        vertic[i] = max_cnt

    max_vertic = 0
    for i in vertic:
        if max_vertic < i:
            max_vertic = i

    if max_vertic < max_horiz:
        print(f'#{tc} {max_horiz}')
    else:
        print(f'#{tc} {max_vertic}')
