#단순 2진 암호코드
import sys
from collections import deque
sys.stdin = open('input.txt')

#암호 담은 딕셔너리
num_dict = {
    '0001101' : 0,
    '0011001' : 1,
    '0010011' : 2,
    '0111101' : 3,
    '0100011' : 4,
    '0110001' : 5,
    '0101111' : 6,
    '0111011' : 7,
    '0110111' : 8,
    '0001011' : 9
}

def check(arr):
    flag = 0 #암호 딕셔너리에 있는 7자리인지 아닌지 판단
    values = deque() #appendleft를 위해 deque로 생성
    for i in range(N):
        answer = []
        for j in range(M-1,-1,-1):
            if arr[i][j] == '1': #j가 암호문 뭉치의 끝
                for k in range(56):
                    values.appendleft(arr[i][j - k]) #거꾸로 돌면서 56개 글자 담음
                cnt = 0
                temp = []                            
                while cnt != len(values): 
                    temp.append(values[cnt]) #7글자씩 묶기 위해 하나씩 넣음
                    cnt += 1
                    if cnt % 7 == 0:
                        if ''.join(temp) not in num_dict: #암호 딕셔너리에 없는 7글자라면
                            flag = 1
                            break
                        else: #암호 딕셔너리에 있는 7글자라면
                            answer.append(num_dict[''.join(temp)]) #temp의 7글자 묶은 뒤 암호 딕셔너리에서 찾아서 answer에 append
                            temp = [] #초기화
                
                odd = 0 #홀
                even = 0 #짝
                for i in range(len(answer)):
                    if i % 2 == 0:
                        even += answer[i]
                    else:
                        odd += answer[i]
        
                if (even * 3 + odd) % 10 == 0: #올바른 형식의 암호라면
                    return f'#{tc} {even+odd}'
                elif flag == 1:
                    return f'#{tc} {0}'


T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split()) #세로, 가로
    arr = [list(input()) for i in range(N)]
    
    print(check(arr))                      
