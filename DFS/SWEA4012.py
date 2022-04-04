#요리사
def dfs(n, alst, blst):
    global ans

    if n == N:
        if len(alst) == len(blst):
            asum = bsum = 0
            for i in range(len(alst)):
                for j in range(len(alst)):
                    asum += arr[alst[i]][alst[j]]
                    bsum += arr[blst[i]][blst[j]]
            if ans > abs(asum - bsum):
                ans = abs(asum - bsum)
        return

    dfs(n+1, alst+[n], blst) #alst에 선택되는 경우
    dfs(n+1, alst, blst+[n]) #blst에 선택되는 경우

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    
    ans = 987654321
    dfs(0, [], [])
    print(f'#{tc} {ans}')    