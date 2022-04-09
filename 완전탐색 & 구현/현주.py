#현주의 상자 바꾸기

T = int(input()) #테스트 케이스 개수
for tc in range(1, T+1):
    a,b = map(int, input().split()) #상자 개수, 반복작업 진행 횟수

    arr = [0] * a #상자 초기화

    for i in range(1, b+1):
        l, r = map(int, input().split())

        for j in range(l-1,r):
            arr[j]= i

    arr = map(str, arr) #join을 위한 형변환

    print('#{} {}'.format(tc, ' '.join(arr)))

