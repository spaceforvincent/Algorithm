#나무 자르기
N, M = map(int, input().split())
trees = list(map(int, input().split()))
start, end = 1, max(trees) #이분탐색 검색 범위 설정

while start <= end: #적절한 벌목 높이를 찾는 알고리즘
    mid = (start+end) // 2
    
    total = 0 #벌목된 나무 총합
    for tree in trees:
        if tree >= mid:
            total += tree - mid
    
    #벌목 높이를 이분탐색
    if total >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)