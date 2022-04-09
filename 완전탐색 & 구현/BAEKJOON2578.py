#빙고

def check():
    flag = 0
    #가로 체크
    for i in range(5):
        if sum(arr[i]) == 0:
            flag += 1
    #세로 체크
    for j in range(5):
        if sum(list((zip(*arr)))[j]) == 0:
            flag += 1
    
    #우하 대각선 체크
    total = 0
    for k in range(5):
        total += arr[k][k]
    if total == 0:
        flag += 1

    #좌하 대각선 체크
    total = 0
    for l in range(5):
        total += arr[l][4-l]
    if total == 0:
        flag += 1
    
    return flag

def game():
    cnt = 0
    while True:
        num = list(map(int, sys.stdin.readline().split()))
        for k in range(5):
            find = False
            for i in range(5):
                if find == True:
                    break
                for j in range(5):
                    if arr[i][j] == num[k]:
                        arr[i][j] = 0
                        find = True
                        break
            cnt += 1            

            if check() >= 3:
                return cnt

import sys
arr = [list(map(int, sys.stdin.readline().split())) for i in range(5)]
print(game())