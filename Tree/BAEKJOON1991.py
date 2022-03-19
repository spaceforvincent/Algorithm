#트리 순회

import sys
 
N = int(sys.stdin.readline())
tree = {}
 
for n in range(N):
    v, left, right = sys.stdin.readline().split()
    tree[v] = [left, right]
 
 
def preorder(v):
    if v != '.':
        print(v, end='')  # root
        preorder(tree[v][0])  # left
        preorder(tree[v][1])  # right
 
 
def inorder(v):
    if v != '.':
        inorder(tree[v][0])  # left
        print(v, end='')  # root
        inorder(tree[v][1])  # right
 
 
def postorder(v):
    if v != '.':
        postorder(tree[v][0])  # left
        postorder(tree[v][1])  # right
        print(v, end='')  # root
 
#항상 A가 루트 노드
preorder('A')
print()
inorder('A')
print()
postorder('A')
