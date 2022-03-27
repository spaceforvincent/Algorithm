#쇠막대기 자르기
T = int(input())
for tc in range(1,T+1):
    parentheses = list(input())
    stack = [] # 여는 괄호만 담기게 되는 스택
    temp = [] # 레이저 담기
    last = [] # 마지막에 들어간 괄호 
    cnt = 0 #막대기 수

    for i in parentheses:
        if not stack:
            stack.append(i)
        elif i == '(':
            stack.append(i)
        else: #닫는 괄호일 때
            if last == '(': #마지막으로 들어간 괄호가 여는 괄호라면 레이저!
                temp.append(stack.pop()+i) #레이저쌍 만들어서 temp에 넣어줌
                cnt += len(temp) * len(stack) # 1 x 현재 layer수 
                temp = []
            else: #마지막으로 들어간 괄호가 닫는 괄호라면 막대기!
                temp.append(stack.pop()+i)  #막대기 만들어서 temp에 넣어줌
                cnt += len(temp) 
                temp = []
        last = i
            
    print(f'#{tc} {cnt}')