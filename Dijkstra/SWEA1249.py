#보급로

def min_dist():
    min_value = 987654321
    x, y = -1, -1
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and D[i][j] < min_value:
                min_value = D[i][j]
                x, y = i, j
    return x, y
 
 
def dijkstra(x, y):
    # 출발점
    D[x][y] = 0
 
    while True:
        # 가중치 최소갑의 좌표 찾기
        x, y = min_dist()
        visited[x][y] = 1
        # 우하단에 도착하면 리턴
        if x == N-1 and y == N-1: return
        # 4방향 탐색, 방문X,
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 인접한 정점 update
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if D[nx][ny] > D[x][y] + arr[nx][ny]:
                    D[nx][ny] = D[x][y] + arr[nx][ny]
 
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    D = [[987654321]*N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    dijkstra(0, 0)
    print(f'#{tc} {D[N-1][N-1]}')