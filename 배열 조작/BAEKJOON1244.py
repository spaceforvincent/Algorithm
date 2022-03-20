#스위치 켜고 끄기

S = int(input()) #스위치 개수
status = list(map(int,input().split())) #스위치 상태
student = int(input()) #학생 수

for i in range(student):
    give = list(map(int,input().split())) #수 나눠주기


    if give[0] == 1:#남학생일 때
        for i in range(give[1], len(status)+1):
            if i % give[1] == 0: #i가 받은 숫자의 배수일 때
                if status[i-1] == 0: #i번째 스위치 변경
                    status[i-1] = 1
                else:
                    status[i-1] = 0

    elif give[0] == 2:#여학생일 때
        i = 1
        while give[1]-1-i >=0 and give[1]-1+i <= S-1: #앞 뒤 인덱스가 인덱스 범위를 넘지않는 동안
            if status[give[1]-1-i] == status[give[1]-1+i]: #대칭이라면
                i += 1 #계속 진행
            else:
                break
        for a in range(give[1]-i, give[1]-1+i): #구간 내 한번에 처리
            if status[a] == 0:
                status[a] = 1
            else:
                status[a] = 0
            

for i in range(len(status)):
    if i in [20,40,60,80,100]:
        print()
    print(status[i], end = ' ')



