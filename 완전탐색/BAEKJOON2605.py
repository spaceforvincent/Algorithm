a = int(input()) #학생 수

b = list(map(int, input().split()))

arr = []
for i in range(a):
    arr.insert(i - b[i], i+1) #삽입할 위치, 삽입할 값

arr = map(str,arr)

print(' '.join(arr))
