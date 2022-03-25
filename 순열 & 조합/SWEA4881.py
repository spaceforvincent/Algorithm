#배열 최소 합
from itertools import combinations

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]

    for j in combinations(arr[i],1):
            print(j)
