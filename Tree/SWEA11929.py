#이진 힙 (최소 힙)

def enq(num): #삽입
    global last
    last += 1 #완전 이진트리 유지 위해 노드 추가
    tree[last] = num

    c = last
    p = last // 2

    while p and tree[p] > tree[c]: #부모 노드 < 자식 노드 유지
        tree[p], tree[c] = tree[c], tree[p] #swap
        c = p
        p = c // 2

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    lst = list(map(int, input().split())) #N개의 자연수

    last = 0 # 힙의 원소의 개수
    tree = [0] * (N+1)
    
    for i in lst:
        enq(i)
    
    total = 0
    while N!=1:
        total += tree[N//2]
        N = N//2
    
    print(f'#{tc} {total}')