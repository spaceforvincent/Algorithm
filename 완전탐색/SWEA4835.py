T = int(input())

for tc in range(1, T + 1):
    a,b = map(int, input().split())  #입력 숫자 개수와 구간 길이
    c = list(map(int, input().split())) #숫자 리스트

    #구간합 담을 리스트
    result = [0] * (len(c)-b+1)

    for i in range(len(c)-b+1): #총 구간 개수동안
        total = 0
        for j in range(0,b) :#구간 길이 만큼
            result[i] = c[i : i+b] #구간 자르기
            total = total + result[i][j] #구간별 합
            result[i] = total

    min_v = result[0]
    max_v = result[0]
    for num in result:
        if max_v<num:
            max_v = num
    for num in result:
        if min_v>num:
            min_v = num
    print(f'#{tc} {max_v - min_v}')