def perm(n, k, a):
    global ans
    
    if a <= ans:  # 곱하는 값들이 1보다 작기때문에 중간까지의 결과값이 ans보다 작으면 앞으로도 가능성 없음
        return

    if n == k:
        if a > ans:
            ans = a
    else:
        for i in range(k):
            if visited[i] == 0:
                visited[i] = 1
                p[n] = i
                perm(n+1, k, a * arr[n][p[n]])
                visited[i] = 0


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    
    for i in range(N):
        arr[i] = list(map(lambda x: x * 0.01, arr[i]))
   
    ans = 0
    
    p = [0] * N
    visited = [0] * N

    perm(0,N,1)
    print(f'#{tc} {ans*100:.6f}')
