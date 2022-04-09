#색종이

'''
3
3 7
15 7
5 2
'''

a = int(input())

point_lst = [list(map(int, input().split())) for i in range(a)]
arr = [[0] * 100 for i in range(100)]

for k in range(a):
    for i in range(point_lst[k][1], point_lst[k][1]+10):
        for j in range(point_lst[k][0], point_lst[k][0]+10):
            arr[i][j] = 1

cnt = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] == 1:
            cnt += 1
print(cnt)