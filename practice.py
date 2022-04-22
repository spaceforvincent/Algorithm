import sys
N = int(sys.stdin.readline())

cnt = 0
while cnt != 2*N:
    for i in range(N):
        print(' ' * (N - (i+1)) + '*' * (2*i+1))
        cnt += 1
    if cnt == N:
        for i in range(N):
            print(' ' * (i+1) + '*' * (2*N - (2*i+3)))
            cnt += 1