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
cnt_arr = [0] * len(lst)
for i in range(len(lst)):
    cnt_arr[i] = lst.count(lst[i])


max_cnt = max(cnt_arr)
ans = lst[cnt_arr.index(max_cnt)]
cnt = 0
for i in range(len(lst)):
    if cnt_arr[i] == max_cnt:
        cnt += 1
        if cnt == 2: 
            ans = lst[i]

print(int((sum(lst) / N)+0.5)) #산술평균
print(lst[len(lst)//2]) #중앙값
print(ans) #최빈값
print(max(lst) - min(lst))#범위
