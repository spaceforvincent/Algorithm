#이진탐색

def inorder(v):
    global last 
    if v <= N:
        inorder(v * 2)
        tree[v] = last
        last += 1
        inorder(v*2 + 1)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    last = 1
    tree = [0] * (N+1)
    inorder(last)
    print(f'#{tc}', tree[1], tree[N//2])
