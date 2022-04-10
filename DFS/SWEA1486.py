#장훈이의 높은 선반
T = int(input())

def dfs(n, total):
    global ans
    #가지치기
    if ans < total - B:
        return 
    
    if n == N:
        if total >= B and ans > total - B: 
            ans = total - B
        return
    dfs(n+1, total+lst[n]) #포함하는 경우
    dfs(n+1, total) #포함하지 않는 경우

for tc in range(1,T+1):
    N, B = map(int, input().split())
    lst = list(map(int, input().split()))
    ans = 987654321 #탑 높이와 B의 차이
    dfs(0, 0)
    
    print(f'#{tc} {ans}')