#벌집
import sys
N = int(sys.stdin.readline())
if N==1:
    print(1)
else:
    cnt = 1
    find_group = [2,2]
    while find_group[0] != N:
        find_group[0] += 1
        cnt += 1
        if cnt == 6 * (find_group[1]-1) + 1:
            find_group[1] += 1
            cnt = 1

    print(find_group[1])