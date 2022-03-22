#프린터 큐
import sys
from collections import deque
T = int(sys.stdin.readline())
for tc in range(1,T+1):
    N,M = map(int, sys.stdin.readline().split()) #문서 개수, 문서가 큐에서 몇번째 놓여있는지
    lst = list(map(int, sys.stdin.readline().split())) #중요도 배열
    
    Q = deque(enumerate(lst)) #(인덱스, 중요도)
    lst.sort(reverse=True) #뽑을 순서대로 정렬
    
    cnt = 1
    while True:
        if Q[0][1] == lst[0]: #Q 맨앞 item의 중요도가 현재 lst에서 가장 큰 값의 중요도와 같다면
            if Q.popleft()[0] == M: #일단 출력하는데 출력한 프린트의 인덱스가 찾으려고 했던 문서의 번호와 같을 때
                break
            cnt += 1 #출력한 횟수
            lst.pop(0) #중요도 최고값 바뀜
        else:
            Q.append(Q.popleft())

    print(cnt)
        

