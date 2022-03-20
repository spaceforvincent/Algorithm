#설탕배달

sugar = int(input())

cnt = 0
while sugar >= 0 :
    if sugar % 5 == 0 :
        cnt += (sugar // 5)  
        print(cnt)
        break
    sugar -= 3  
    cnt += 1  # 5의 배수가 될 때까지 설탕-3, 봉지+1
else :
    print(-1)