#연산
from collections import deque

def bfs(v):
    Q = deque()
    Q.append(v)
    visited[v] = 1
    while Q:
        v = Q.popleft()
        if v == M:
            return visited[v] - 1
        else:
            choice = [v + 1, v - 1, v * 2, v - 10]
            for i in range(len(choice)):
                if choice[i] > 0 and choice[i] <= 1000000 and visited[choice[i]] == 0:
                    Q.append(choice[i])
                    visited[choice[i]] = visited[v] + 1

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split()) #시작, 목표

    visited = [0] * 1000001

    print(f'#{tc} {bfs(N)}')