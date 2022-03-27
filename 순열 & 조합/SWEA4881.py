#배열 최소 합
from itertools import permutations

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]

    min_sum = 999
    for perm in permutations(list(range(0,N))):
        total = 0
        for i in range(0,N):
            total += arr[i][perm[i]] #각 줄의 각 순열 원소번째 수 더함
            if total >= min_sum: #가지치기
                break

        if total < min_sum: #최솟값 갱신
            min_sum = total
    
    print(f'#{tc} {min_sum}')
