#새로운 버스 노선

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    cnt_arr = [0] * 1000 #최대 정류장번호 : 1000
    for i in range(N):
        line = list(map(int, input().split()))
        
        if line[0] == 1: #일반버스인 경우
            for i in range(line[1],line[2]+1):
                cnt_arr[i] += 1
        elif line[0] == 2: #급행버스인 경우
            for i in range(line[1],line[2]+1):
                if line[1] %2 : #출발이 홀수인 경우
                    if i%2:
                        cnt_arr[i] += 1 
                else: #출발이 짝수인 경우
                    if i%2 == 0:
                        cnt_arr[i] += 1 
        else: #광역버스인 경우
            for i in range(line[1],line[2]+1):
                if line[1] %2 : #출발이 홀수인 경우
                    if i%3 == 0 and i%10:
                        cnt_arr[i] += 1
                else: #출발이 짝수인 경우
                    if i%4 == 0:
                        cnt_arr[i] += 1

    print(f'#{tc} {max(cnt_arr)}')        
