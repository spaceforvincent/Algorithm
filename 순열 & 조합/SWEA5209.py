#최소 생산 비용

def perm(n, k, t):
    global ans

    if t >= ans:
        return

    if n == k:
        if t < ans:
            ans = t
    else:
        for i in range(k):
            if visited[i] == 0:
                visited[i] = 1
                p[n] = i
                perm(n+1, k, t + arr[n][p[n]])
                visited[i] = 0


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    ans = 9999999
    p = [0] * (N)
    visited = [0] * (N)

    perm(0, N, 0)
    print(f'#{tc} {ans}')