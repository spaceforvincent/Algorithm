#View

import sys
sys.stdin = open('building_input.txt')

T=10
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    ans = 0
    #왼쪽과 오른쪽으로 창문을 열었을 때, 양쪽 모두 거리 2 이상의 공간이 확보될 때 조망권이 확보
    for i in range(2,N-2): #빌딩 각각에서(양 옆 0 2개씩 빼고)
        if arr[i] <= arr[i+1] or arr[i] <= arr[i-1]: #일단 현재 그 빌딩이 양 옆의 건물보다 층수가 낮거나 층수가 같다면 애초에 탈락
            pass
        # 현재 그 빌딩이 양 옆과 그 다음 양 옆의 건물보다 높다면 일단 꼭대기 조망권 확보. 그 아래 층수도 조망권이 확보되는지 확인해야함.
        elif arr[i] > arr[i-1] and arr[i] > arr[i+1] and arr[i] > arr[i-2] and arr[i] > arr[i+2]:
            #양 옆 2개씩의 건물들 중 가장 높은 층 수 구하기
            max_value = arr[i-2] #일단 초기화
            lst = [arr[i-2],arr[i-1],arr[i+1],arr[i+2]] #거리 2 안에 들어오는 건물 리스트
            cnt = 0
            for v in lst:
                if max_value < v:
                    max_value = v
            cnt = arr[i]-max_value #각 빌딩에서의 조망권 세대 수
            ans += cnt
    print(f'#{tc} {ans}')