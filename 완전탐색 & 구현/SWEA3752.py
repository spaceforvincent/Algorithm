#가능한 시험점수

T = int(input())
for tc in range(1, T+1):
    N = int(input()) #시험 문항 수
    scores = list(map(int, input().split())) #문항 별 점수
    answer = [0] #0점부터 시작
    
    for score in scores:
        answer = list(set(answer)) #중복 점수 제거
        for i in range(len(answer)):
            answer.append(answer[i]+score)

    print(f'#{tc} {len(set(answer))}')