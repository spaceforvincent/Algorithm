#삼성시의 버스 노선

T = int(input())
for tc in range(1,T+1):
    N = int(input()) #버스 노선 개수
    cnt = [0] * 5001
    for i in range(N):
        stop1, stop2 = map(int, input().split())#정류장 범위1
        for j in range(stop1,stop2+1):
            cnt[j] += 1
    
    ans = []
    P = int(input()) #궁금한 버스 정류장 개수
    for i in range(P):
        ans.append(cnt[int(input())])

    print(f'#{tc}', *ans)
