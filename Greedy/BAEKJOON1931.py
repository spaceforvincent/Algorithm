#회의실 배정
import sys

N = int(sys.stdin.readline())
time_lst = []
for i in range(N):
    time_lst.append(list(map(int, sys.stdin.readline().split())))

time_lst.sort(key = lambda x: (x[1],x[0])) #종료시간으로 오름차순 정렬 

cnt = 0   #연속해서 작업 가능한 횟수  
ans = []  #타임테이블
for i in range(len(time_lst)):
    if not ans: #아직 ans에 아무것도 안들어있다면
        ans.append(time_lst[i])
        cnt += 1
    elif time_lst[i][0] >= ans[-1][1] : 
        ans.append(time_lst[i])
        cnt += 1

print(cnt)