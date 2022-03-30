#컨테이너 운반

def load():
    ans = 0
    while w_lst and sum(t_lst) != 0: #더 이상 담을 컨테이너 없거나 트럭 다 사용했을 때까지      
        for i in range(len(t_lst)):
            for j in range(len(w_lst)):
                if t_lst[i] >= w_lst[j]:
                    ans += w_lst[j]
                    w_lst.pop(0) #담은 트럭 있으니 pop
                    t_lst[i] = 0 #트럭 사용 표시 
                    break
                else: #트럭 적재용량보다 컨테이너가 무거운 경우
                    break
        
        if not w_lst: #더 이상 담을 컨테이너 없다면
            break
        
        w_lst.pop(0) #어느 트럭도 담을 수 없는 무게였던 경우
    
    return ans

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split()) #컨테이너 수, 트럭 수
    w_lst = sorted(list(map(int, input().split())), reverse = True) #화물의 무게 내림차순 정렬
    t_lst = sorted(list(map(int, input().split())), reverse = True) #트럭 적재 용량 내림차순 정렬
    
    
    print(f'#{tc} {load()}')
