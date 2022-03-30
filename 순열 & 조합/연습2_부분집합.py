# 부분집합의 합이 10이 되는 부분집합을 출력하시오.
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(arr)
cnt = 0
for i in range(1 << n):  # 0 ~ 7
    # 부분집합의 합 구하기
    sum = 0
    for j in range(n):
        if i & (1 << j):
            sum += arr[j]

    # sum 10일때, 출력
    if sum == 10:
        for j in range(n):
            if i & (1 << j):
                print(arr[j], end=', ')
        print()
        cnt += 1

print(f'count : {cnt}')