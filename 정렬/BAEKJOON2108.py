#통계학
'''
5
1
3
8
-2
2
'''
import sys

N=int(sys.stdin.readline())

lst = []
for i in range(N):
    lst.append(int(sys.stdin.readline()))

lst.sort()

print(int(round(sum(lst) / len(lst),1))) #산술평균
print(lst[len(lst)//2]) #중앙값

print(max(lst) - min(lst))#범위
