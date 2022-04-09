#직사각형 네개의 합집합의 면적 구하기

point_lst = [list(map(int, input().split())) for i in range(4)]
arr = [[0] * 100 for i in range(100)]

for k in range(4):
    for i in range(point_lst[k][1],point_lst[k][3]):
        for j in range(point_lst[k][0],point_lst[k][2]):
            arr[i][j] = 1

cnt = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] == 1:
            cnt += 1
print(cnt)
            

    
    