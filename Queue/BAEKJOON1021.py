#회전하는 큐
import sys
from collections import deque

N,M = map(int, sys.stdin.readline().split()) #큐의 크기, 뽑아내려고 하는 개수
target = list(map(int, sys.stdin.readline().split()))

Q = deque(range(1,N+1))

cnt = 0
while True:
    if Q[0] == target[0]: #Q 맨앞 값이 현재 타겟과 같을 때
        Q.popleft()
        target.pop(0) #타겟값 변경
    elif Q.index(target[0]) >= len(Q)/2: #타겟의 인덱스가 인덱스 중앙값보다 뒤에 있을 때는 오른쪽으로 돌리는게 유리
        Q.appendleft(Q.pop())
        cnt += 1 #큐 돌린 횟수 증가
    elif Q.index(target[0]) < len(Q)/2: #타겟의 인덱스가 인덱스 중앙값보다 앞에 있을 때는 왼쪽으로 돌리는게 유리
        Q.append(Q.popleft())
        cnt += 1 #큐 돌린 횟수 증가
    if not target: #타겟값 다 출력했다면
        break

print(cnt)
