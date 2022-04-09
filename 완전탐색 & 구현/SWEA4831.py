#Bus

import sys
sys.stdin = open('bus_input.txt')

T=int(input()) #테스트 횟수
for tc in range(1, T+1):
    k,n,m = map(int, input().split()) #한번 충전으로 최대한 이동할 수 있는 정류장 수 K, 종점 N, 충전기가 설치된 정류장 개수 M
    charge = list(map(int, input().split())) #충전기 설치된 버스정류장 세팅

    course = [0] * (n+1)
    for i in range(len(course)):
        course[i] = i #경로

    cnt = 0 #충전횟수
    battery = k #시작시 충전
    for i in range(1,len(course)): #i가 커질때마다(코스 한칸씩 갈 때마다)
        battery -= 1 #배터리 감소
        for j in range(len(charge)):
            if course[i] == charge[j]: #가는 도중에 충전기를 만났을 때
                if charge[j] == charge[-1]: #마지막 충전소일때
                    if n - charge[j] <= battery: #목적지까지 갈만큼 배터리가 충분히 남아있다면
                        pass
                    else: #아니라면 충전
                        battery = k
                        cnt += 1
                elif battery < charge[j+1] - charge[j] : #남은 배터리가 현재 충전소부터 다음 충전소까지의 거리보다 적을 때(마지막 충전소 제외한 경우)
                    battery = k #배터리 충전
                    cnt += 1
                else: #남은 배터리가 다음 충전소까지의 거리보다 많거나 같을 때 이번 충전소 패스
                    pass

    for j in range(len(charge)-1):
        if charge[j+1]-charge[j] > k or n - charge[-1] > k: #안되는 경우
            cnt = 0
            break
    print(f'#{tc} {cnt}')