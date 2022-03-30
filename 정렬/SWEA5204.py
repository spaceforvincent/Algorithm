'''
2
5
2 2 1 1 3
10
7 5 4 1 2 10 3 6 9 8
'''    

def merge_sort(a):

    global cnt
    if len(a) == 1: 
        return a
    
    else:
        mid = len(a) // 2
        left = a[:mid]
        right = a[mid:]

        left = deque(merge_sort(left))
        right = deque(merge_sort(right))

        result = []    
        if left[-1] > right[-1]:
            cnt += 1
        while left or right:
            # 두 리스트가 모두 존재하면
            if left and right:
                if left[0] <= right[0]:
                    result.append(left.popleft())
                else:
                    result.append(right.popleft())
            # 왼쪽리스트만 존재
            elif left:
                result.append(left.popleft())
            # 오른쪽만 존재
            elif right:
                result.append(right.popleft())

        return result

from collections import deque
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    arr = merge_sort(arr)   
    print(f'#{tc} {arr[N//2]} {cnt}')