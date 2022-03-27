#단어순서 뒤집기
import sys

case = int(sys.stdin.readline())
for c in range(1,case+1):
    result = []
    something = sys.stdin.readline().split()

    for i in range(len(something)-1,-1,-1):
        result.append(something[i])

    print(f'Case #{c}:', *result)
