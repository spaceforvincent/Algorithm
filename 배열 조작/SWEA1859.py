#백만장자 프로젝트
                 
T = int(input())
for tc in range(1,T+1):
    day = int(input())
    prices = list(map(int,input().split()))
    last = prices[-1]
    income = 0
    for i in range(len(prices)-1,-1,-1): #뒤부터 보기
        if last > prices[i]: 
            income += last - prices[i] #차익
        else: # 비교중인 가격보다 큰 가격 등장 
            last = prices[i] #새로운 가격
    print(f'#{tc} {income}')
 


