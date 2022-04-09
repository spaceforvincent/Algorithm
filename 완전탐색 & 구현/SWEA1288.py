#새로운 불면증 치료법

a = int(input()) #테스트 횟수
target = list(map(str,list(range(10)))) #최종결과와 비교할 리스트 (같으면 while 종료)

for i in range(a):    
    n = 1 #n 초기화
    lst = [] #리스트 초기화
    inp = input() #최초 입력
    while True:    
        b = str(int(inp) * n) #분해하기 위해 str형 변환
        c = list(b) #하나하나 분해
        for num in c:
            if num in lst: #이미 있다면
                continue
            else:
                lst.append(num) #숫자 추가
        if sorted(lst) == target: #같다면 while 종료
            break
        n += 1
    
    print(f'#{i+1} {n*int(inp)}')


