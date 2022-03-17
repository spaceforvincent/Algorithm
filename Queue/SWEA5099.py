#피자 굽기
from collections import deque   
 
T = int(input())
for tc in range (1,T+1):
    N, M = map(int, input().split()) #화덕 크기, 피자 개수
    pizza = list(enumerate(list(map(int, input().split())))) #인덱스 문제 필수템..
    cnt = 0
 
    Q = deque(pizza[:N]) #화덕크기만큼 담아주고 시작
    cnt += N #pizza리스트에서 꺼내서 지금까지 담은 개수 기록
     
    while len(Q) > 1: #마지막에 하나 남을 때까지
        if Q[0][1] == 0: #치즈가 다 녹았을 때
            if cnt >= M: #이미 pizza리스트에서 다 꺼냈다면
                Q.popleft() #꺼내주기만 함
            else: #아직 pizza리스트에 남아있다면
                Q.popleft()
                Q.appendleft(pizza[cnt]) #꺼내고 다음차례 피자 넣어줌
                cnt += 1 #넣은 개수 증가 기록
        else: #치즈 덜 녹았을 때
            x = Q.popleft()
            Q.append((x[0],x[1]//2))
            continue
     
    print(f'#{tc} {Q[0][0]+1}')