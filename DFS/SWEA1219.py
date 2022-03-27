#길찾기

import sys
sys.stdin = open('swea1219_input.txt')

def dfs(now):
    global flag
    if now == 99: #종료조건
        flag = 1
        return

    visited[now] = 1 #방문 체크

    for next in adj[now]:
        if visited[next] == 0: # next노드가 방문했는지?
            dfs(next)


for i in range(10):
    flag = 0
    tc, N = map(int,input().split()) #테스트 번호, 길 총 개수
    draw = list(map(int, input().split()))

    adj = [[] for _ in range(100)]  # 인접리스트 초기화
    visited = [0] * (100)  # 방문처리 

    # 인접리스트 저장하기
    for i in range(N):
        s, e = draw[2 * i], draw[2 * i + 1]
        adj[s].append(e)

    print(adj)

    dfs(0)
    print(f'#{tc} {flag}')