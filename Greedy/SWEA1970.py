#쉬운 거스름돈
T = int(input())
for tc in range(1,T+1):
    a = int(input()) #나눌 돈

    cashier = [50000, 10000, 5000, 1000, 500, 100, 50,10]
    cnt = [0] * len(cashier)

    for c in range(len(cashier)):
        if a < cashier[c]:
            continue
        else:
            cnt[c] += (a // cashier[c])
            a = a - ((a//cashier[c])*cashier[c])
            continue
    print(f'#{tc}')
    print(*cnt)

        