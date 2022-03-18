#사칙연산
import sys
sys.stdin = open('input.txt')

def postorder(v):
    global stack
    if tree[v]:
        postorder(left[v])
        postorder(right[v])
        if type(tree[v]) == int: #피연산자라면        
            stack.append(tree[v])
        else: #연산자라면
            a = stack.pop()
            b = stack.pop()
            if tree[v] == '+':
                stack.append(b+a)
            elif tree[v] == '-':
                stack.append(b-a)
            elif tree[v] == '*':
                stack.append(b*a)
            else:
                stack.append(b/a)

for tc in range(1,11):
    
    N = int(input()) #정점의 총 수
    tree = [0] * (N + 1) #연산자 & 피연산자 담김
    left = [0] * (N + 1)
    right = [0] * (N + 1)

    for i in range(N):
        lst = input().split()    
        if len(lst) == 4:
            tree[int(lst[0])] = lst[1] #연산자
            left[int(lst[0])] = int(lst[2]) #왼쪽 자식
            right[int(lst[0])] = int(lst[3]) #오른쪽 자식
        elif len(lst) == 2:
            tree[int(lst[0])] = int(lst[1]) #피연산자

    stack = []
    postorder(1)
    print(f'#{tc} {int(stack[0])}')     
    
        
