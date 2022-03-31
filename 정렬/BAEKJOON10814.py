#나이 순 정렬

import sys

N = int(sys.stdin.readline())

lst = []
for i in range(N):
    age_and_name = sys.stdin.readline().split()
    lst.append(age_and_name)

lst = list(enumerate(lst))

lst.sort(key = lambda x : (int(x[1][0]),x[0]))

for i in lst:
    print(f'{i[1][0]} {i[1][1]}')