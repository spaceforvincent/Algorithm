# Greedy

- 현재 상황에서 지금 당장 좋은 것만 고르는 방법
- 현재의 선택이 나중에 미칠 영향에 대해서는 고려하지 않음
- 보통 코테의 그리디 알고리즘 유형의 문제는 창의력을 요구한다
- 문제 풀이를 위한 최소한의 아이디어를 떠올리고 이것이 정당한지 검토할 수 있어야 답을 도출할 수 있다.
- 문제에서 ''가장 큰 순서대로'', ''가장 작은 순서대로''와 같은 기준을 알게 모르게 제시해준다. ex) 거스름돈



예제1 - 큰 수의 법칙

```
#큰 수의 법칙
import sys

N, M, K = map(int, sys.stdin.readline().split()) #배열 크기, 숫자가 더해지는 횟수, 연속해서 더할 수 있는 횟수

arr = list(map(int, sys.stdin.readline().split()))

arr = sorted(arr, reverse=True)

ans = 0
cnt = 0
while cnt != M:
    if cnt != 0 and cnt % K == 0:
        ans += arr[1]
        cnt == 0
    else:
        ans += arr[0]
    cnt += 1

print(ans)
```



예제2 - 숫자 카드 게임

```
#숫자 카드 게임
#각 행마다 가장 작은 수를 찾은 뒤에 그 수 중에서 가장 큰수를 찾는 아이디어
import sys
N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for i in range(N)]

for i in range(N):
    arr[i] = sorted(arr[i])

maxV = 0
for i in range(N):
    if maxV < arr[i][0]:
        maxV = arr[i][0]

print(maxV)
```



예제3 - 1이 될때까지

```
#1이 될때까지
#최대한 많이 나누기
#1이 될때까지

import sys
N, K = map(int, sys.stdin.readline().split())

cnt = 0
while N != 1:
    if N % K != 0:
        N -= 1
        cnt += 1
    else:
        N /= K
        cnt += 1

print(cnt)


```

