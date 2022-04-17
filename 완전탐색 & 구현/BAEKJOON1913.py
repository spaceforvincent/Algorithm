#달팽이

# di = [0,1,0,-1]
# dj = [1,0,-1,0]


# N = int(input())
# target = int(input())
# arr = [[0] * N for i in range(N)]

# cnt = 1
# end = N**2

# arr[0][0] = 49
# i = 0
# j = 0
# while cnt != end:
#     for k in range(4):
#         for a in range(N-1):
#             ni = i + di[k]
#             nj = j + dj[k]
#             if 0<=ni<=N-1 and 0<=nj<=N-1 and arr[ni][nj] == 0:
#                 arr[ni][nj] = arr[i][j] -1
#                 i = ni
#                 j = nj    
#                 cnt+=1
      
# for i in range(len(arr)):
#     print(*arr[i])
