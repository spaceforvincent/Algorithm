#전자카트

#꼬리에 꼬리 물면서 이어지네...

from itertools import permutations

#1. itertools
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    
    ans = 999
    for perm in permutations(list(range(1,N))): #1부터 N까지 만들수 있는 순열
        total = arr[0][perm[0]] #arr 첫번째 행의 각 perm의 첫번째 원소 위치의 비용 더해주고 시작
        for j in range(len(perm)-1): #꼬리 물기
            total += arr[perm[j]][perm[j+1]] 
        total += arr[perm[-1]][0] #마지막은 arr 첫번쨰열로 돌아와야함 

        if total < ans: #현재 정답보다 total이 작다면
            ans = total #new 정답
            
    print(f'#{tc} {ans}')


#2. 순열 만들기
def perm(n, k): # n:배열크기, k:깊이
    global min_sum
    total = 0
    if n == k:
        for i in range(len(p)-1):
            total += arr[p[i]][p[i+1]]
        if min_sum > total:
            min_sum = total
    else:
        for i in range(1, n):
            if visited[i] == 0:
                visited[i] = 1
                p[k] = idx_lst[i]
                perm(n, k+1)
                visited[i] = 0
    
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    min_sum = 999
    idx_lst = list(range(0,N))

    p = [0] * (N+1) #0번 행에서 시작해서 0번째 열로 돌아온다
    visited = [0] * (N+1)
    visited[0] = 1

    perm(N, 1)
    print(f'#{tc} {min_sum}')
