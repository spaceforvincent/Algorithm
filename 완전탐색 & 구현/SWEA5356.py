#의석이의 세로로 말해요
T = int(input())
for tc in range(1,T+1):
    arr = [list(input()) for i in range(5)]

    max_cnt = 0
    for i in range(len(arr)):
        cnt = 0
        for j in range(len(arr[i])):
            cnt += 1
        if max_cnt < cnt:
            max_cnt = cnt

    for i in range(len(arr)):
        if len(arr[i]) < max_cnt:
            arr[i] = arr[i] + ['+'] * (max_cnt - len(arr[i])) #그 줄에서 모자란 부분은 +로 채움

    ans = []
    for j in range(max_cnt):
        for i in range(5):
            if arr[i][j] == '+': #+면 담지 않음
                continue
            else:
                ans.append(arr[i][j])
    print(f'#{tc}', ''.join(ans))
