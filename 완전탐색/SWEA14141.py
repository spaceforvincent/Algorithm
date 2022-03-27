#이진수1

#16 -> 10 -> 2

dic_16 = {   
    'A' : 10,
    'B' : 11,
    'C' : 12,
    'D' : 13,
    'E' : 14,
    'F' : 15
    }

def get_binnum(m):
    lst = []
    a = m
    while a != 0 :
        a = m // 2
        b = m % 2
        lst.append(str(b))
        m = a
    return lst

T = int(input())
for tc in range(1,T+1):
    N, target = input().split()
    
    lst_10 = [] #10진수 담을 리스트
    for i in range(int(N)):
        if target[i] in dic_16: #알파벳이라면
            lst_10.append(dic_16[target[i]])
        else: #숫자라면
            lst_10.append(target[i])
    
    lst_10 = list(map(int, lst_10))
    
    ans = []
    for num in lst_10:
        if len(get_binnum(num)) <= 3:
            ans.append((get_binnum(num)+['0']*(4-len(get_binnum(num))))[::-1])
        else:
            ans.append(get_binnum(num)[::-1])


    final_ans = ''.join(sum(ans, []))

    print(f'#{tc} {final_ans}')
    





