a = int(input()) #테스트 개수

scores = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0'] #학점 리스트

for t in range(a):
    b = list(map(int, input().split())) #학생수와 성적 알고 싶은 학생 번호 입력받기
    lst = [] #총점 담을 리스트
    for i in range(b[0]):
        c = list(map(int, input().split())) #각각의 학생이 받은 시험 및 과제 점수 입력 받기
        total = (c[0] * 0.35) + (c[1] * 0.45) + (c[2] * 0.2) #총점 = (중간 * 35%) + (기말 * 45%) + (과제 * 20%)
        lst.append(total)
    
    target_score = lst[b[1]-1] #입력한 학생번호의 점수

    sorted_lst = sorted(lst,reverse=True) #성적 분배 위해 점수 리스트 내림차순 정렬
    n = b[0]//10 #테스트 별 동일한 평점 받는 학생 수
    g = sorted_lst.index(target_score) // n # 성적 그룹

    print(f'#{t+1} {scores[g]}')
