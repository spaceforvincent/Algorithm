# 종이 붙이기

#1. DP
def put(n):  # 남은 너비, 현재 너비
    lst = [0] * (n+1)
    lst[0] = lst[1] = 1
    for i in range(2, n+1):
        lst[i] = lst[i-2] * 2 + lst[i-1]
    return lst[n]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    print(f'#{tc} {put(N // 10)}')


# 2. 재귀(제한시간 초과)
# T = int(input())
# for tc in range( 1,T+1):
#     w = int(input())  # 채워야 하는 직사각형 밑변 너비
#     cnt = 0  # 방법 수

#     def put(remain, now):  # 남은 너비, 현재 너비
#         if remain == 0 and now == w:  # 꽉 찼다면
#             global cnt
#             cnt += 1
#             return  # 함수 실행 위치로 되돌아감

#         put(remain - 10, now + 10)  # 기본 넣는 방식 : 10x20 세로로 넣기
#         if remain >= 20:  # 채워야 할 남은 너비가 20보다 클 때
#             put(remain - 20, now + 20)  # 20x20짜리 1개 넣음
#             put(remain - 20, now + 20)  # 10x20짜리 2개 가로로 넣은 경우('='이렇게)
#         return  # 함수 실행 위치로 되돌아감


#     put(w, 0)
#     print(f'#{tc} {cnt}')
