#노드의 합

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    N,M,L = map(int,input().split()) #노드의 개수, 리프 노드의 개수, 값을 출력할 노드 번호
    tree = [0] * (N+1)
    
    for i in range(M):
        leaf, num = map(int, input().split())
        tree[leaf] = num
    
    for i in range(N,0,-1):
        if tree[i] == 0:
            if 2*i == N :
                tree[i] = tree[2*i]
            else:    
                tree[i] = tree[2*i] + tree[2*i + 1]

    print(f'#{tc} {tree[L]}')

    
