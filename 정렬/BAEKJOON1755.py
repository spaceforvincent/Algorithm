#숫자놀이

dict = {
        '1' : 'one', 
        '2' : 'two', 
        '3' : 'three', 
        '4' : 'four', 
        '5' : 'five', 
        '6' : 'six', 
        '7' : 'seven', 
        '8' : 'eight', 
        '9' : 'nine', 
        '0' : 'zero'
        }
dict2 = {
        'one' : '1', 
        'two' : '2', 
        'three' : '3', 
        'four' : '4', 
        'five' : '5', 
        'six' : '6', 
        'seven' : '7', 
        'eight' : '8', 
        'nine' : '9', 
        'zero' : '0'}

import sys
a, b = map(int, sys.stdin.readline().split())
lst = list(map(str, list(range(a, b+1))))

#숫자를 영어단어로 바꾼다
arr = []
for i in range(len(lst)):
    temp = []
    for j in range(len(lst[i])):
        temp.append(lst[i][j].replace(lst[i][j], dict[lst[i][j]]))
    arr.append(''.join(temp))

#사전 순서대로 정렬한다
arr.sort()

#영어단어를 숫자로 바꾼다
ans = []
for i in range(len(arr)):
    temp = []
    temp2 = []
    for j in range(len(arr[i])):
        temp.append(arr[i][j])
        if ''.join(temp) in dict2:
            temp2.append(arr[i][:j].replace(arr[i][:j], dict2[''.join(temp)]))
            temp = []
    ans.append(''.join(temp2))

#10줄마다 줄바꿈해서 출력
cnt = 0
for i in ans:
    print(i, end = ' ')
    cnt += 1    
    if cnt == 10:
        print()
        cnt = 0