#subtree

def count(v):
    global cnt
    if v:
        cnt += 1
        count(left[v])
        count(right[v])
        

T = int(input())
for tc in range(1,T+1):
    E, N = map(int, input().split()) #간선 개수, 루트로 할 노드
    lst = list(map(int, input().split()))
    cnt = 0

    left = [0] * (E+2)
    right = [0] * (E+2)

    for i in range(E):
        p, c = lst[2*i], lst[2*i+1]
        if left[p]: #이미 왼쪽자식에 값이 있다면
            right[p] = c #부모의 오른쪽 자식은 c
        else:
            left[p] = c #부모의 왼쪽 자식은 c

    count(N)
    print(f'#{tc} {cnt}')

