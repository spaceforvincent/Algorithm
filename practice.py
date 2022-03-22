import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

if N < 2:
    print('Before')
else :
    if N == 2 and M > 18:
        print('After')
    elif N == 2 and M < 18:
        print('Before')
    elif N > 2:
        print('After')
    elif N == 2 and M == 18:
        print('Special')
