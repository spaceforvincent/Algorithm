#베이비진 게임

def check():
    global player1, player2
    for i in range(len(arr)):
        if i % 2 == 0: #player1
            player1.append(arr[i])
            if i >= 4:
                player1.sort()
                player1_s = sorted(list(set(player1)))
                for j in range(len(player1_s) - 2):
                    if (player1_s[j] + 2 == player1_s[j+1] + 1 == player1_s[j+2]):
                        return 1
                for k in range(len(player1)-2):
                    if (player1[k] == player1[k+1] == player1[k+2]): 
                        return 1
                            
        else: #player2
            player2.append(arr[i])
            if i >= 5:
                player2.sort()
                player2_s = sorted(list(set(player2)))
                for j in range(len(player2_s) - 2):
                    if (player2_s[j] + 2 == player2_s[j+1] + 1 == player2_s[j+2]):
                        return 2
                for k in range(len(player2)-2):
                    if (player2[k] == player2[k+1] == player2[k+2]): 
                        return 2
    
    return 0

T = int(input())
for tc in range(1,T+1):
    arr = list(map(int, input().split())) 
    player1 = []
    player2 = []

    print(f'#{tc} {check()}')