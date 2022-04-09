import sys
sys.stdin = open('sum_input.txt')

T=10
for tc in range(1,T+1):
    a = int(input()) #순서
    arr = [list(map(int,input().split())) for _ in range(100)]

    horiz_sum_lst = [0] * 100
    vertic_sum_lst = [0] * 100

    for i in range(len(arr)):
        horiz_sum = 0
        vertic_sum = 0
        diagonal_sum1 = 0
        diagonal_sum2 = 0
        for j in range(len(arr)):
            horiz_sum += arr[i][j]
            vertic_sum += arr[j][i]
            diagonal_sum1 += arr[j][j]
            diagonal_sum2 += arr[j][4-j]
 
        horiz_sum_lst[i] = horiz_sum
        vertic_sum_lst[i] = vertic_sum

    max_horiz = 0
    for n in range(len(horiz_sum_lst)):
        if max_horiz < horiz_sum_lst[n]:
            max_horiz = horiz_sum_lst[n]
    max_vertic = 0
    for m in range(len(vertic_sum_lst)):
        if max_vertic < vertic_sum_lst[m]:
            max_vertic = vertic_sum_lst[m]
        
    result_lst = [max_horiz, max_vertic, diagonal_sum1, diagonal_sum2]

    max_v = 0
    for k in range(len(result_lst)):
        if max_v < result_lst[k]:
            max_v = result_lst[k]

    print(f'#{tc} {max_v}')