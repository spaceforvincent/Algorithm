def fibonacci(N):
    if N==0:
        return 0
    elif N <= 2:
        return 1
    else:
         return fibonacci(N-1) + fibonacci(N-2)

import sys
N = int(sys.stdin.readline())

print(fibonacci(N))