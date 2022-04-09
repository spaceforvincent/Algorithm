#퍼펙트 셔플

T = int(input())

for tc in range(1,T+1):
    N = int(input()) #배열 길이
    arr = input().split()
    
    insert_lst = []
    
    if len(arr) % 2 == 0: #배열 길이가 짝수일 때 
        for i in range(len(arr)):
            if i >= len(arr) // 2:
                insert_lst.append(arr[i])
        arr = arr[:len(arr)//2]
    
    else: #배열 길이가 홀수 일 때
        for i in range(len(arr)):
            if i >= (len(arr) // 2)+1:
                insert_lst.append(arr[i])    
        arr = arr[:(len(arr)//2)+1]
    

    for i in range(len(insert_lst)):
        arr.insert(2*i+1,insert_lst[i])

    arr = ' '.join(arr)

    print(f'#{tc} {arr}')

