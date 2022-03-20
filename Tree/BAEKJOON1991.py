#트리 순회

import sys
 
N = int(sys.stdin.readline())
tree = {}
 
for n in range(N):
    v, left, right = sys.stdin.readline().split()
    tree[v] = [left, right]
 
 
def preorder(v):
    if v != '.':
        print(v, end='')  
        preorder(tree[v][0]) 
        preorder(tree[v][1])  
 
 
def inorder(v):
    if v != '.':
        inorder(tree[v][0])  
        print(v, end='')  
        inorder(tree[v][1])  
 
 
def postorder(v):
    if v != '.':
        postorder(tree[v][0])  
        postorder(tree[v][1])  
        print(v, end='')  
 
#항상 A가 루트 노드
preorder('A')
print()
inorder('A')
print()
postorder('A')
