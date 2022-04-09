# 파리 퇴치

T = int(input())  # 테스트 횟수

for tc in range(1,T+1):
    b, c = map(int, input().split())  # b x b배열과 c x c 파리채

    # 배열 입력
    arr = [list(map(int, input().split())) for i in range(b)]

    # 구간합 담을 리스트 만들기(가로)
    horiz_stick = [[0] * (b - c + 1) for i in range(b)]

    # 가로 구간합 구하기
    for i in range(b):
        for j in range(b - c + 1):
            horiz_guganhap = 0
            for k in range(c):
                horiz_guganhap += arr[i][j + k]
            horiz_stick[i][j] = horiz_guganhap
    
    # 세로 구간합 구하기 (가로 구간합 리스트 바탕으로)
    result = 0
    for i in range(b - c + 1):
        for j in range(b - c + 1): 
            vertic_guganhap = 0
            for k in range(c):
                vertic_guganhap += horiz_stick[j + k][i]
            if result < vertic_guganhap:
                result = vertic_guganhap  
    
    print(f'#{tc} {result}')