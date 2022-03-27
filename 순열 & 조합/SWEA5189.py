#전자카트
from itertools import permutations

#꼬리에 꼬리 물면서 이어지네...
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    
    ans = 999
    for perm in permutations(list(range(1,N))): #1부터 N까지 만들수 있는 순열
        total = arr[0][perm[0]] #arr 첫번째 행의 각 perm의 첫번째 원소 위치의 비용 더해주고 시작
        for j in range(len(perm)-1): #꼬리 물기
            total += arr[perm[j]][perm[j+1]] 
        total += arr[perm[-1]][0] #마지막은 arr 첫번쨰열로 돌아와야함 

        if total < ans: #현재 정답보다 total이 작다면
            ans = total #new 정답
            
    print(f'#{tc} {ans}')