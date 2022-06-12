#최대공약수, 최소공배수
import sys
N,M = map(int, sys.stdin.readline().split())

answer1 = []
a = 1
for i in range(min(N,M)):
    if N % (a+i) == 0 and M % (a+i) == 0:
        answer1.append(a+i)



answer2 = 0
while True:
    new_N = N
    new_N *= a
    if new_N % M == 0:
        answer2 = new_N
        break
    a += 1

print(max(answer1))
print(answer2)