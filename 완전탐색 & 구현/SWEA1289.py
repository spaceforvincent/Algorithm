#원재의 메모리 복구

#초기화된 상태 : 0 0 0 0

T = int(input())
for tc in range(1,T+1):
    original = list(map(int,input()))
    reset = [0] * len(original)

    cnt = 0
    while reset != original:
        for i in range(len(original)):
            if original[i] == 0:
                if reset[i] == 0:
                    continue
                else:
                    for j in range(i,len(reset)):
                        reset[j] = 0
                    cnt+=1
            else:
                if reset[i] == 1:
                    continue
                else:
                    for j in range(i,len(reset)):
                        reset[j] = 1
                    cnt+=1
    print(f'#{tc} {cnt}')

