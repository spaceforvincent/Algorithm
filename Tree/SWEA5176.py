#이진 탐색

#이진탐색

def inorder(v):
    global last 
    if v <= N:
        inorder(v * 2)
        tree[v] = last
        last += 1
        inorder(v*2 + 1)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    last = 1
    tree = [0] * (N+1)
    inorder(last)
    print(f'#{tc}', tree[1], tree[N//2])

#트리의 성질 이용

import math

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    k = int(math.log2(N)) + 1 # 전체 트리의 층 수

    #루트 노드 값 찾기
    if N >= 2**(k-1) + (2**(k-1))/2 -1 : #N이 층 맨 앞 노드의 인덱스랑 그 인덱스를 반 나눈것의 합보다 크거나 같다면
        ans1 = 2**(k-1)
    else:
        ans1 = N - (2**(k-2)-1) 

    
    #리프 노드 만들기
    leaf = [[0] * (2**i) for i in range(k)]

    #리프 노드의 값들은 1,3,5,7...로 고정!
    for i in range(len(leaf[int(math.log2(N))])):
        leaf[int(math.log2(N))][i] = 2*i+1
    
    #루트노드에서부터 세었을 때 N번째 노드 수 찾기
    cnt = 0
    for i in range(len(leaf)):
        for j in range(len(leaf[i])):
            cnt+= 1
            if cnt == N: #N번째 노드 찾았을 때
                if j % 2 == 0:
                    ans2 = leaf[i][j]+1 #찾은 N번째 노드가 그 층에서 짝수번째 인덱스일때
                else:
                    ans2 = leaf[i][j]-1 #찾은 N번째 노드가 그 층에서 홀수번째 인덱스일때

    if N == 1:
        print(f'#{tc} {ans1} {1}')   
    else:
        print(f'#{tc} {ans1} {ans2}')

        
