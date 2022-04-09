import sys
sys.stdin = open('중력_input.txt')

T = int(input())
for tc in range(1,T+1):
    N= int(input())
    arr = list(map(int, input().split()))
    ans = 0

    for i in range(N): #꼭대기값들
        #i의 최대 낙차값 : N-1-i
        #i 이후의 모든 행을 검사한다.
        max_height = N - 1 - i
        for j in range(i+1,N):
            #아래(다음) 행이 i행보다 상자가 많거나 같으면 최대 낙차값에서 1 감소
                if arr[i] <= arr[j]:
                    max_height -= 1
        #낙차 값의 최대값을 구하기
        if ans < max_height:
            ans = max_height

    print(f'{tc} {ans}')
