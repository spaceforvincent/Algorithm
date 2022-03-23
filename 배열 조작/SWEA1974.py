#스도쿠 검증

import sys
sys.stdin = open('swea1974_input.txt')

T=int(input())
for tc in range(1, T+1):

    #스도쿠 조건 : 가로 세로, 겹치는 숫자 없이 1~9까지 다 있어야 함, 3x3 퍼즐 안에서 1~9 겹치면 안됨

    puzzle_lst_horiz = [] #스도쿠 퍼즐 가로 검사
    for i in range(1,10):
        b = list(map(int, input().split())) #스도쿠 퍼즐
        puzzle_lst_horiz.append(b)

    puzzle_lst_vertic = list(zip(*puzzle_lst_horiz))

    # 3x3 만들기 (여기서 너무 오래 걸렸음)
    puzzle = []
    for i in range(0,9): 
        for j in range(0,9,3):
            puzzle.append(puzzle_lst_horiz[i][j:j+3])
    
    puzzle_3x3 = [] #모든 줄에 대한 3x3 퍼즐
    for k in range(0,len(puzzle)-6):
        puzzle_3x3.append(puzzle[k]+puzzle[k+3]+puzzle[k+6])

    new_puzzle_3x3 = [] #range 조정을 통한 3x3 퍼즐 9개 제작 완료
    for i in range(0,len(puzzle_3x3),9):
        new_puzzle_3x3.append(puzzle_3x3[i:i+3])
    
    last_puzzle_3x3 = [] #깔끔하게 정리
    for i in range(len(new_puzzle_3x3)):
        for lst in new_puzzle_3x3[i]:
            last_puzzle_3x3.append(lst)


    for i in range(len(puzzle_lst_horiz)):
        if len(list(set(puzzle_lst_horiz[i]))) != 9 or len(list(set(puzzle_lst_vertic[i]))) != 9 or len(list(set(last_puzzle_3x3[i]))) != 9: #가로, 세로, 3x3 검사
            ans = 0
            break
        else:
            ans = 1

    print(f'#{tc} {ans}')
    
        
        
        
        
        
        
        
        # for j in range(len(puzzle_lst[i])):
        #     if j not in list(range(1,10)):
        #         break