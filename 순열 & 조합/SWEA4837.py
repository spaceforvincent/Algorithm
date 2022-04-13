#부분집합의 합

# from itertools import combinations
    

# T = int(input())
# for tc in range(1,T+1):
#     lst = list(range(1,13))
#     N, K = map(int, input().split()) #원소의 수, 부분집합의 합
#     cnt = 0
    
#     for comb in combinations(lst,N):
#         if sum(comb) == K:
#             cnt += 1

#     print(f'#{tc} {cnt}')


def dfs(n, total):

    global cnt

    if n >= N:
        if total == K:
            cnt += 1
        return

    dfs(n+1, total + lst[n])
    dfs(n+1, total)




T = int(input())
for tc in range(1,T+1):
    lst = list(range(1,13))
    print(lst)
    N, K = map(int, input().split()) #원소의 수, 부분집합의 합
    cnt = 0
  
    dfs(0,0)
    print(cnt)