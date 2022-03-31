#이진 탐색
T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split()) #A 원소 개수, B 원소 개수
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))

    cnt = 0
  
    for i in range(M):
        l = 0
        r = N-1
        flag_l = 0
        flag_r = 0
        while l<=r:
            m = (l + r)//2
            if A[m] == B[i]:
                cnt += 1
                break
            elif A[m] < B[i]:
                if flag_r == 1:
                    break
                else:
                    l = m + 1
                    flag_l = 0
                    flag_r = 1
            elif A[m] > B[i]:
                if flag_l == 1:
                    break
                else:
                    r = m - 1
                    flag_r = 0
                    flag_l = 1

    print(f'#{tc} {cnt}')