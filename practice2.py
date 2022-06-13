#소트인사이드
import sys
N = list(map(int, list(sys.stdin.readline().rstrip())))

N = sorted(N,reverse=True)

N = list(map(str, N))

print(''.join(N))