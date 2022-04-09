#정곤이의 단조 증가하는 수

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))
 
    max_value = -1
    for i in range(N):
        for j in range(i+1, N):
            if i == j:
                continue
            else:
                value = str(arr[i] * arr[j])
                if len(value) == 1: #한자리 수 인 경우
                    max_value = int(value) if max_value < int(value) else max_value
                for j in range(len(value)-1):
                    if value[j] > value[j+1]:
                        break
                else: #value[j] <= value[j+1]인 경우(단조증가하는 경우)
                    max_value = int(value) if max_value < int(value) else max_value
 
    print(f'#{tc} {max_value}')