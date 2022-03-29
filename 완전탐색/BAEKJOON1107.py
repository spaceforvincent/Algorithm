#리모컨
import sys

def plus_minus():
    cnt_min = 1
    cnt_max = 1
    start_min = broken[0] - 1
    while start_min != target[i]:
        start_min += 1
        cnt_min += 1
    start_max = broken[-1] + 1
    while start_max != target[i]:
        start_max -= 1
        cnt_max += 1
    
    return min(cnt_min,cnt_max)
    

target = list(map(int, list(sys.stdin.readline().rstrip())))
M = int(sys.stdin.readline()) #고장난 버튼 개수

cnt = 0
lst = [1,0,0] #현재 채널 : 100

- (''.join(lst))

if len(lst) < len(target):
    lst = [0] * len(target) - len(lst) + lst
elif len(lst) > len(target):
    lst = [0] * len(target) - len(lst) + lst

if M:
    broken = sorted(list(map(int, sys.stdin.readline().split())))
for i in range(len(target)):
    if M:
        if target[i] not in broken:
            cnt += 1
            lst[i] = target[i]
        else:
            cnt += plus_minus()
    else:
        cnt += 1
        lst[i] = target[i]

print(cnt)
