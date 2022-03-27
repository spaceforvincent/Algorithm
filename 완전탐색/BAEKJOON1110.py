#더하기 사이클

input = input()
if int(input) < 10: #input이 10보다 작을 때 두자리수 만들어주기
    input = '0' + input

base = input #while 내에서 사용할 input을 새로운 변수로 정의
count = 0 #더한 횟수
plus = '00' #더한 수 초기화
new_num = '00' #새로운 수 초기화

while input != new_num: #input과 new_num이 같아질 때까지
    plus = str(int(base[0]) + int(base[1])) #각 자릿수 더하기
    count += 1 #더한 횟수 + 1
    if int(plus) < 10: #plus가 0보다 작다면 두자리수 만들어주기
        plus = '0' + plus
    new_num = base[1] + plus[1] #주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙이면 새로운 수
    base = new_num
    
if int(input) == 0:
    print(1)
else:
    print(count)