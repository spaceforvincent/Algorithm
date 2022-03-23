#AC
import sys
from collections import deque
T = int(sys.stdin.readline()) #테스트 횟수
for tc in range(1,T+1):
    commands = sys.stdin.readline().rstrip() #명령들
    n = int(sys.stdin.readline()) #배열에 들어있는 수의 개수
    Q = deque(list(sys.stdin.readline().rstrip()[1:-1].split(','))) #앞 뒤 대괄호 제거, 쉼표 기준 분리 
    if n == 0: #빈 배열이 들어왔다면
        Q = deque()
    
    #뒤집는 횟수를 최소화하자!
    flag = 0 #에러 표시할지 말지 결정
    rev_cnt = 0 #R이 홀수개만큼 있으면 뒤집고 R이 짝수개만큼 있으면 뒤집지 말자!
    
    for command in commands:
        if command == 'R':
            rev_cnt += 1
        elif command == 'D':
            if not Q:
                flag = 1
                break
            else:
                if rev_cnt % 2 == 0: #R이 짝수개만큼 있어서 뒤집지 않는 경우
                    Q.popleft() #큐 앞에서 제거
                else:
                    Q.pop() #큐 뒤에서 제거
    
    if flag == 1:
        print('error')
    else:
        if rev_cnt % 2 :
            Q.reverse()
        print('[{}]'.format(','.join(Q)))