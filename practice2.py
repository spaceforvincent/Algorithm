#야구

#문제 이해하고 들어가는 것을 목표로...!!!
#줄의 맨 처음 인덱스는 4번타자가 치는 결과로 고정
#4번 타자 앞 3명 타자, 뒤 5명만 순열로 순서 바꿔주면서 돌린다?

import sys


innings = int(sys.stdin.readline())

result = [list(map(int, sys.stdin.readline().split())) for i in range(innings)]

for i in range(innings):
    result[i].insert(3,result[i].pop(0))

#획득 가능 점수
ans = 0 

#0이 세번 나오면 이닝 종료
zero_cnt = 0

# 몇 명의 주자가 필드에 나가 있는가?
base_1 = 0
base_2 = 0 
base_3 = 0

last_idx = 0 #아웃된 번쨰 기억

inning = 0
while inning != innings:
    for i in range(innings):
        for j in range(last_idx, 9):
            if result[j] == 0:
                zero_cnt += 1
                if zero_cnt == 3:
                    last_idx = j
                    inning += 1
                    break
            elif result[j] == 1:
                base_1 += 1
            elif result[j] == 2:
                base_2 += 1
            elif result[j] == 3:
                base_3 += 1
            elif result[j] == 4:
                ans += base_1 + base_2 + base_3 + 1
            if j == 9:
                last_idx = 0

print(ans)       
