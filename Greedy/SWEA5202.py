#화물 도크
T = int(input())
for tc in range(1,T+1):
    N = int(input()) #신청서 개수
   
    time_lst = []
    for i in range(N):
        time_lst.append(list(map(int, input().split())))

    time_lst.sort(key= lambda x : (x[1], x[0])) #종료시간으로 오름차순 정렬 

    cnt = 0   #연속해서 작업 가능한 횟수  
    ans = []  #타임테이블
    for i in range(len(time_lst)):
        if not ans: #아직 ans에 아무것도 안들어있다면
            ans.extend(list(range(time_lst[i][0],time_lst[i][1])))
            cnt += 1
        elif time_lst[i][0] > ans[-1] : 
            ans.extend(list(range(time_lst[i][0],time_lst[i][1])))
            ans = sorted(ans)
            cnt += 1

    
    print(f'#{tc} {cnt}')