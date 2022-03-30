#동전 0
import sys

N, target = map(int, sys.stdin.readline().split())

cashier = []
for i in range(N):
    cashier.append(int(sys.stdin.readline()))

cashier.sort(reverse=True) #내림차순 정렬

cnt = [0] * len(cashier) #동전개수만큼 카운트 배열 만들기

for i in range(len(cashier)):
    if target < cashier[i]: #거스름돈이 타켓보다 더 클 때
        continue
    else:
        cnt[i] += (target // cashier[i]) #준 동전 개수만큼 플러스
        target = target - ((target//cashier[i])*cashier[i]) #남은 "줘야할 돈" 감소

print(sum(cnt))