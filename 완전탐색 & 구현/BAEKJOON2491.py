#수열

import sys
N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

max_cnt = 0
bigger_flag = 1
smaller_flag = 1
cnt = 0
for i in range(N-1):
    if lst[i+1] >= lst[i] and smaller_flag:  
        bigger_flag = 1
        smaller_flag = 0
        if bigger_flag:
            cnt += 1
    elif lst[i+1] <= lst[i] and bigger_flag:  
        smaller_flag = 1
        bigger_flag = 0
        if smaller_flag:
            cnt += 1

print(max_cnt)