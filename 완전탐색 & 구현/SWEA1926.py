#간단한 369게임 

n = int(input()) #n
lst = []
for i in range(1,n+1):
    lst.append(i)


lst = list(map(str,lst))
for k in range(len(lst)): #문자로 변환된 숫자 리스트에서
    for j in range(len(lst[k])): #한 숫자 한 숫자 보면서
        if list(lst[k])[j] in ['3','6','9']: #만약 그 숫자에 3이나 6이나 9가 있으면
            cnt3 = lst[k].count('3')
            cnt6 = lst[k].count('6')
            cnt9 = lst[k].count('9')
            sum_cnt = cnt3 + cnt6+ cnt9
            lst[k] = lst[k].replace(lst[k],'-' * sum_cnt) #3이나 6이나 9가 나온 횟수만큼 -를 넣어줘야 함
            if lst[k] == '-':
                break
print(' '.join(lst))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # if lst[k][j] in ['3','6','9']: #만약 그 숫자에 3이나 6이나 9가 있으면
        #     cnt3 = lst[k][j].count('3')
        #     cnt6 = lst[k][j].count('6')
        #     cnt9 = lst[k][j].count('9')
        #     sum_cnt = cnt3 + cnt6+ cnt9
        #     lst[k] = lst[k].replace(lst[k],'-' * sum_cnt) #3이나 6이나 9가 나온 횟수만큼 -를 넣어줘야 함

            
   
    