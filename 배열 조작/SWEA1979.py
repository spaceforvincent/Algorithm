#어디에 들어갈 수 있을까

import sys
sys.stdin = open('1979_input.txt')

def cnt_cnt(arr,N):
    
    cnt_cnt = 0

    #가로 체크
    cnt_lst = [] #숫자 세서 담을 리스트
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j] == 1:
                cnt+=1
            else: #0이라면
                cnt_lst.append(cnt)
                cnt = 0
                continue
        cnt_lst.append(cnt)

    
    for c in cnt_lst:
        if c == K:
            cnt_cnt += 1

    #세로 체크
    cnt_lst = []    
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[j][i] == 1:
                cnt+=1
            else: #0이라면
                cnt_lst.append(cnt)
                cnt = 0
                continue
        cnt_lst.append(cnt)
    
    
    for c in cnt_lst:
        if c == K:
            cnt_cnt += 1
    
    return cnt_cnt

    

T = int(input())
for tc in range(1,T+1):
    N, K = map(int, input().split()) #배열 크기, 단어 길이
    arr = [list(map(int, input().split())) for i in range(N)]
    
    print(f'#{tc} {cnt_cnt(arr,N)}')