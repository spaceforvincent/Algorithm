#파스칼의 삼각형

a = int(input()) #테스트 횟수

for i in range(a):
    n = int(input()) #삼각형 줄 개수
    result_lst = [] #삼각형 결과 담을 리스트
    for j in range(1,n+1):
        if j <= 2: #삼각형의 2번째 줄까지는
            lst = [1] * j
            result_lst.append(lst)
        else:
            lst = [0] * j #초기화
            lst[0] = lst[-1] = 1 #줄의 맨앞 맨뒤는 1로 고정
            for k in range(1,len(lst)-1): #맨 앞과 맨 뒤 사이
                lst[k] = result_lst[-1][k-1] + result_lst[-1][k] #삼각형 바로 윗줄에서의 좌우 숫자 연산 값 가져오기
            result_lst.append(lst)
    
    print(f'#{i+1}') #출력형식
    for l in range(len(result_lst)):
        result_lst[l] = list(map(str, result_lst[l]))
        print(' '.join(result_lst[l]))
    
    
    
            

