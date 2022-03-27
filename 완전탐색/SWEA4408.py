#자기 방으로 돌아가기
import sys 
T = int(input()) 
for tc in range(1, T+1): 
    N = int(input()) 
    # 사용 중인 복도를 표시할 리스트 
    corridor = [0] * 200 
    # 방 위치를 복도를 기준으로 바꾸어서 카운팅 
    for n in range(N): 
        room = list(map(int, input().split()))
        for i in range(2): 
            if room[i] % 2: #홀수번 방번호라면 
                room[i] = (room[i] - 1) // 2 #맞닿아 있는 corridor
            else: #짝수번 방번호라면
                room[i] = (room[i] - 2) // 2 #맞닿아 있는 corridor
        if room[0] <= room[1]: 
            for j in range(room[0], room[1]+1): 
                corridor[j] += 1 
        else: 
            for j in range(room[1], room[0]+1): 
                corridor[j] += 1 
    
    print(f'#{tc} {max(corridor)}')
