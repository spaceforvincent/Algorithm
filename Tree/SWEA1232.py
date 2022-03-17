#사칙연산
import sys
sys.stdin = open('input.txt')

def postorder():
    pass


T = 10
for tc in range(1,T+1):
    
    N = int(input()) #정점의 총 수
    operator = [0] * (N + 1)
    left = [0] * (N + 1)
    right = [0] * (N + 1)
    operand = [0] * (N + 1) 


    for i in range(N):
        lst = input().split()
        if len(lst) == 4:
            operator[int(lst[0])] = lst[1] #연산자
            left[int(lst[0])] = lst[2] #왼쪽 자식
            right[int(lst[0])] = lst[3] #오른쪽 자식
        elif len(lst) == 2:
            operand[int(lst[0])] = lst[1] #피연산자

    print(operator)
         
        
    
        
