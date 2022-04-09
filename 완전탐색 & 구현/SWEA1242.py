#암호 패턴
patterns = {
(3,2,1,1) : 0,
(2,2,2,1) : 1,
(2,1,2,2) : 2,
(1,4,1,1) : 3,
(1,1,3,2) : 4,
(1,2,3,1) : 5,
(1,1,1,4) : 6,
(1,3,1,2) : 7,
(1,2,1,3) : 8,
(3,1,1,2) : 9,
}
hex_dic = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',
          '4': '0100', '5': '0101', '6': '0110', '7': '0111',
          '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
          'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}


T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    data = [list(input()) for _ in range(N)]

    # 16진수를 4비트 바이너리로 바꿔서 새로운 배열 만들기
    arr = []
    for i in range(N):
        row = ''
        for j in range(M):
            row += hex_dic[data[i][j]]
        arr.append(row)

    result = 0
    for i in range(N):
        idx = 4*M - 1   # 입력받은 16진수를 4비트 바이너리로 바꿨으니 길이가 4배 늘어남
        while idx >= 55:
            if arr[i][idx] == '1' and arr[i-1][idx] == '0':   #패턴 시작
                password = []
                for _ in range(8):
                    c1 = c2 = c3 = c4 = 0 # 패턴의 각 부분의 길이
                    # 1의 개수 세서 c4에 저장
                    while arr[i][idx] == '1':
                        c4 += 1
                        idx -= 1
                    # 0의 개수 세서 c3에 저장
                    while arr[i][idx] == '0':
                        c3 += 1
                        idx -= 1
                    # 1의 개수 세서 c2에 저장
                    while arr[i][idx] == '1':
                        c2 += 1
                        idx -= 1
                    # 0의 개수를 세서 c1에 저장
                    rate = min(c2,c3,c4)    
                    #최소비율이 모두 1기 때문에 최소값을 찾으면, 곱해진 배율을 찾을 수 있음
                    c2 //= rate
                    c3 //= rate
                    c4 //= rate
                    c1 = 7 - c2 - c3 - c4
                    idx -= c1*rate
                    #패턴 구했으니! >> 숫자 찾기
                    password.insert(0, patterns[(c1,c2,c3,c4)])
                print(password)
                odd_sum = password[0] + password[2] + password[4] + password[6]
                even_sum = password[1] + password[3] + password[5] + password[7]

                if (odd_sum * 3 + even_sum) % 10 == 0:
                    result += odd_sum + even_sum
            else:
                idx -= 1
    print(f'#{tc}  {result}')