#Flatten

import sys
sys.stdin = open('Flatten_input.txt')

T=10
for tc in range(1, T+1):
    dump = int(input()) #덤프 횟수
    arr = list(map(int, input().split())) #박스 세팅

    # 가장 높은 곳에서 가장 낮은 곳으로 준다
    while dump > 0:
        dump -= 1

        max_height = arr[0]
        for j in range(len(arr)):
            if max_height <= arr[j]:
                max_height = arr[j]  # 초기 상자 높이 최댓값
                max_idx = j

        min_height = arr[0]
        for k in range(len(arr)):
            if min_height >= arr[k]:
                min_height = arr[k]  # 초기 상자 높이 최솟값
                min_idx = k

        arr[max_idx] -= 1
        arr[min_idx] += 1

        if arr[max_idx] - arr[min_idx] <= 1:
            break
    max_height = arr[0]
    for j in range(len(arr)):
        if max_height <= arr[j]:
            max_height = arr[j]  # 초기 상자 높이 최댓값
            max_idx = j

    min_height = arr[0]
    for k in range(len(arr)):
        if min_height >= arr[k]:
            min_height = arr[k]  # 초기 상자 높이 최솟값
            min_idx = k

    print(f'#{tc} {max_height - min_height}')