#나이 순 정렬

import sys

def bubble_sort(lst):
    for i in range(len(lst) - 1, 0, -1):
        for j in range(i):
            if int(lst[j][0]) > int(lst[j + 1][0]):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst
N = int(sys.stdin.readline())

lst = []
for i in range(N):
    age_and_name = tuple(sys.stdin.readline().split())
    lst.append(age_and_name)

for i in range(len(lst))