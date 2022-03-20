#막대기
#스택과 입력 감 잡기

import sys
n = int(sys.stdin.readline())
data = [int(sys.stdin.readline()) for i in range(n)]

max_h = data[-1]
visible_lst = [data[-1]] #오른쪽에서 봤을 때 첫번째 막대기는 무조건 보이니까 담고 시작
for h in range(len(data)-1,-1,-1):
    if data[h] > max_h:
        max_h = data[h]
        visible_lst.append(data[h])
    else:
        continue

print(len(visible_lst))