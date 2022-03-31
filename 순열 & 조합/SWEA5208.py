from itertools import permutations

T = int(input())
for tc in range(1,T+1):
    arr = list(map(int, input().split()))
    dest= arr[0]
    charge = arr[1:]

    ans = 999

    for perm in permutations(charge):
        total = perm[0]
        cnt = 0
        for i in range(1,len(perm)):
            total += perm[i]
            cnt += 1
            if total >= dest:
                if ans > cnt:
                    ans = cnt
                    break
            if cnt > ans:
                break
                         
    print(f'#{tc} {ans}')