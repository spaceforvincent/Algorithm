#이진수2

def get_binnum(N):
    lst = []
    while str(N)[-1] != '0':
        N = float(N) * 2
        lst.append(str(N)[0])
        N = '0.'+str(N)[2:]
        if len(lst) >= 13:
            return 'overflow'
    return lst


T = int(input())
for tc in range(1,T+1):
    N = input()

    ans = ''.join(get_binnum(N))

    print(f'#{tc} {ans}')