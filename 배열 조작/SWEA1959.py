#두개의 숫자열
import sys
sys.stdin = open('swea1959_input.txt')

T=int(input())
for tc in range(1, T+1):
    t,b = map(int, input().split()) #위 배열 길이, 아래 배열 길이
    lst1 = list(map(int, input().split()))
    lst2 = list(map(int, input().split()))

    if len(lst1) < len(lst2):
        max_lst = lst2
        min_lst = lst1
    else:
        max_lst = lst1
        min_lst = lst2


    #구간 자르기(짧은 것 길이만큼 긴 것 길이를 구간으로 자른다)
    gugan = [[0] * min(t,b) for i in range(max(t,b) - min(t,b)+1)]
    
    for i in range(len(gugan)): #lst1과 lst2 중 길이가 짧은 것을 움직이자
            gugan[i] = max_lst[i:i+min(t,b)]
    
    #곱셈
    ans_lst = []
    for i in range(len(gugan)):
        for j in range(len(min_lst)):
            gugan[i][j] = min_lst[j] * gugan[i][j]
        ans_lst.append(sum(gugan[i]))

    print(f'#{tc} {max(ans_lst)}')
