#리모컨

target = int(input())
# 고장난 번호 개수
M = int(input())

# a는 target에서 하나씩 올라가는 채널, b는 하나씩 내려가는 채널
a = b = target

# answer는 target에서 현재 채널까지의 거리로 초기화
answer = abs(target - 100)
 
if M :  # 고장난 번호가 1개 이상일 때 고장난 번호 입력받기
    broken = list(map(int,input().split()))

    # 타겟 채널이 고장나지 않은 번호들로만 구성되어 있으면 1
    flag = 0

    # 입력받은 채널로부터 위로 아래로 한칸씩 가며 고장나지 않은 번호들로 구성되어 있을 때
    # 번호 길이와 , 정답 채널과의 거리 차이를 더해 answer와 비교하여 작은 값을 출력
    while True:
        # a
        if b >= 0 :
            b_list = list(map(int,str(b))) #한 글자씩
            for i in set(b_list):
                if i in broken:
                    b -= 1
                    break
            else:
                flag = 1

            if answer < len(str(b)) + target - b :
                print(answer)
                break

            if flag == 1:
                print(len(str(b)) + target - b)
                break
            
        a_list = list(map(int,str(a)))
        
        if broken:
            for i in set(a_list):
                if i in broken:
                    a += 1
                    break
            else:
                flag = 1
        
        if answer < len(str(a)) + a - target :
                print(answer)
                break

        if flag == 1:
            print(len(str(a)) + a- target)
            break
# 고장나지 않았다면 정답채널과 100채널 사이의 거리와 정답채널의 길이를 비교하여 작은 값을 출력
else:
    print(min(answer, len(str(target))))

# def plus_minus():
#     cnt_min = 1
#     cnt_max = 1
#     start_min = broken[0] - 1
#     while start_min != target[i]:
#         start_min += 1
#         cnt_min += 1
#     start_max = broken[-1] + 1
#     while start_max != target[i]:
#         start_max -= 1
#         cnt_max += 1
    
#     return min(cnt_min,cnt_max)


# import sys
# target = list(map(int, list(sys.stdin.readline().rstrip())))
# M = int(sys.stdin.readline()) #고장난 버튼 개수
# cnt = 0

# if M:
#     broken = sorted(list(map(int, sys.stdin.readline().split())))

# for i in range(len(target)):
#     if target[i] not in broken:
#         cnt += 1
#     else:
#         cnt += plus_minus()         
    
# print(cnt)
# # # import sys
    

# # # target = list(map(int, list(sys.stdin.readline().rstrip())))
# # # M = int(sys.stdin.readline()) #고장난 버튼 개수

# # # cnt = 0
# # # lst = [1,0,0] #현재 채널 : 100


# # # if M:
# # #     broken = sorted(list(map(int, sys.stdin.readline().split())))
# # # for i in range(len(target)):
# # #     if M:
# # #         if target[i] not in broken:
# # #             cnt += 1
# # #             lst[i] = target[i]
# # #         else:
# # #             cnt += plus_minus()
# # #     else:
# # #         cnt += 1
# # #         lst[i] = target[i]

# # # print(cnt)
