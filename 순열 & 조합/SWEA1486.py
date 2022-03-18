#장훈이의 높은 선반(조합)
from itertools import combinations 

T = int(input())
for tc in range(1,T+1):
    N, B = map(int, input().split())
    data = list(map(int, input().split()))
    
    min_v = 999999999999
    for i in range(1,N+1):
        for j in combinations(data,i):
            if sum(j) >= B:
                if min_v > sum(j) - B:
                    min_v = sum(j) - B
    
    print(f'#{tc} {min_v}')
