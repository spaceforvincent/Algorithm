'''
3
5 2 3 1 1
10 2 1 3 2 2 5 4 2 1
10 1 1 2 1 2 2 1 2 1
'''

def busstop(n):
    global ans, cnt
    
    if cnt >= ans : #가지치기
        return
      
    if n >= dest: #목적지에 도착하면
        if ans > cnt:
            ans = cnt
    else:
        for i in range(n + arr[n], n, -1):
            cnt += 1 #충전을 하는 경우
            busstop(i)
            cnt -= 1 #충전을 하지 않는 경우

T = int(input())
for tc in range(1,T+1):
    arr = list(map(int, input().split()))
    
    dest= arr[0]
    charge = arr[1:]

    ans = 999
    cnt = 0
    
    busstop(1)
    
    print(f'#{tc} {ans-1}')
