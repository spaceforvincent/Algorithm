#오큰수
#탑 문제와 비슷한 로직으로 푼 것 같음...에휴
import sys
N = int(sys.stdin.readline())
arr = list(enumerate(map(int,sys.stdin.readline().split())))
stack = []
answer = [0] * N

for i in range(len(arr)):
    num = arr[i][1]
    while stack and  num > stack[-1][1]:
        answer[stack[-1][0]] = num
        stack.pop()
    stack.append(arr[i])

for i in range(len(answer)):
    if answer[i] == 0:
        answer[i] = -1

print(*answer)