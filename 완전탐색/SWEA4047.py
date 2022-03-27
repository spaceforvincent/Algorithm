#영준이의 카드카운팅

T = int(input())

for tc in range(1,T+1):
    cards = list(input())
    shape = {'S' : 0, 'D' : 1, 'H' : 2, 'C' : 3}
    ans = [[] for i in range(4)]
    
    for i in range(0,len(cards),3): 
        ans[shape[cards[i]]].append(''.join(cards[i:i+3]))

    for i in range(len(ans)):
        if len(ans[i]) != len(set(ans[i])): #카드중복이 있다면
            ans = ['ERROR']
            break
        else:
            ans[i] = 13-len(ans[i])
    
    print(f'#{tc}', *ans)