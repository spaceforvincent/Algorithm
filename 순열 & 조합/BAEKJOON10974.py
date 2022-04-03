#모든 순열
import sys

def perm(n,k):
    if n == k:
        print(*p)
    else:
        for i in range(k):
            if visited[i] == 0:
                visited[i] = 1
                p[n] = arr[i]
                perm(n+1, k)
                visited[i] = 0 

N = int(sys.stdin.readline())
arr = list(range(1,N+1))
p = [0] * N
visited = [0] * N

perm(0, N)