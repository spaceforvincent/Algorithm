#진기의 최고급 붕어빵
T = int(input())

for tc in range(1,T+1):
    N, M, K = map(int, input().split()) #붕어빵 먹는 사람 수, M초 걸려 K개 만듬
    cust = list(map(int, input().split()))
    
    cust.sort()
    result = 'Possible'
    for i in range(len(cust)):
        b = cust[i]//M * K #cust[i]초일 때 만들어져있는 빵의 개수 (안팔았다고 가정했을 때)
        if b < (i+1): #빵 개수보다 손님 수가 많을 때
            result = 'Impossible'
            break

    print(f'#{tc} {result}')