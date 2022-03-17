"""
13 12
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
"""
def print_tree():
    for i in range(1, V+1):
        print(f'{i:2} | {tree[i][0]:2} {tree[i][1]:2} {tree[i][2]:2}')

def pre_order(node):
    if node != 0 :
        print(node, end=' ')
        pre_order(tree[node][0])
        pre_order(tree[node][1])
    return


V, E = map(int, input().split())
# 인접리스트
tree = [[0] * 3 for _ in range(V+1)]
arr = list(map(int, input().split()))

for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
    if tree[p][0] == 0: # 왼쪽자식이 없으면
        tree[p][0] = c
    else:               # 왼쪽자식이 있으면
        tree[p][1] = c

    tree[c][2] = p

print_tree()
pre_order(1)
