#중위순회

import sys
sys.stdin = open('input.txt')

def in_order(v):
    if v <= N : 
        in_order(v*2) #왼쪽
        print(arr[v], end='')
        in_order(v*2+1) #오른쪽
    return


T = 10
for tc in range(1,T+1):
    
    N = int(input()) #정점의 개수 
    arr = [0] * (N+1)
    for i in range(N):
        data = input().split()
        v = int(data[0])
        alpha = data[1]
        arr[v] = alpha

    print(f'#{tc}', end = ' ')
    in_order(1)
    print()