#탑

'''
5
6 9 5 7 4
'''
import sys

n = int(sys.stdin.readline())
lights = list(enumerate(map(int, sys.stdin.readline().split())))
answer = [0] * n
stack = []

for i in range(n-1,-1,-1): #거꾸로 접근
    light = lights[i]
    while stack and stack[-1][1] < light[1]: #스택이 비어있지 않고 스택 꼭대기에 있는 등대의 높이가 현재 등대 높이보다 낮을 때
        answer[stack[-1][0]] = light[0]+1
        stack.pop()
    stack.append(lights[i]) #스택이 비어있거나 스택 꼭대기에 있는 등대의 높이가 현재 등대의 높이보다 높을 때 스택에 쌓임

print(*answer)