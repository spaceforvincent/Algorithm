t = int(input())

for i in range(t):
    n = int(input())  # 소인수분해 대상

    lst = [2, 3, 5, 7, 11]
    result = [0] * 5

    while n >= 2:
        for m in range(len(lst)):
            if str(n / lst[m])[-1] != '0':  # 안나누어떨어진다면
                continue
            else:
                n = n / lst[m]  # 돌아가면서 나눔
                result[m] += 1  # 나누는 수의 lst 인덱스에 있는 result 값 올라감

    result = map(str, result)  # 값들 떨어뜨려놓기 위해 str변환
    ans = ' '.join(result)

    print(f'#{i + 1} {ans}')