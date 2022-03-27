#연월일 달력
a = int(input())

date_lst = [] #날짜 받기
for i in range(a):
    b = list(input().split())
    date_lst.append(b)

month_list = list(map(int, range(1,13))) #비교 위한 리스트

for i in range(len(date_lst)):
    if int(date_lst[i][0][4:6]) not in month_list : #date_list의 월 부분이 month_list에 들어있지 않다면 '-1'
        date_lst[i][0] = '-1'
    elif date_lst[i][0][4:6] == '02': 
        if int(date_lst[i][0][6:8]) > 28: #date_list의 월 부분이 2월달이고 일 부분이 28일을 넘어설 때 '-1'
            date_lst[i][0] = '-1' 
    date_lst[i] = date_lst[i][0][0:8] #date_lst의 원소들이 ['20220123']의 형식으로 되어있는데 컨테이너 안의 부분만 가져와서 바꿈

def calender(lst):
    result = []
    for i in range(len(lst)):
        if lst[i] != '-1': #'-1'값이 아니라면, 즉 정상적인 날짜형식이라면
            lst[i] = list(lst[i]) #문자열은 immutable하므로 list로 형식을 바꿔줘서 인덱스 자리에 슬래시를 넣어준다.
            lst[i].insert(4, '/')
            lst[i].insert(7, '/')
            lst[i] = ''.join(lst[i]) #문자열 하나로 합치기
        result.append(lst[i])
    return result

final = list(enumerate(calender(date_lst),start = 1)) #인덱스를 1부터 시작하여 리스트 원소 불러옴

for i in range(a):
    print(f'#{final[i][0]} {final[i][1]}')
