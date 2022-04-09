#한수
def d(a):
    lst = []
    for i in range(len(str(a))):
        b = a % 10 #자리 수
        c = a // 10 #남은 수
        lst.append(b)
        a = c
    return lst
    

a = int(input())
hansu_lst = [] #한수 리스트

for num in range(0,a+1): 
    difference_lst = [] #차이 리스트
    if num >= 1 and num < 100:
        hansu_lst.append(num)
        continue
    for i in range(len(d(num))-1): #0,1 
        difference = d(num)[i+1] - d(num)[i]
        difference_lst.append(difference)
    if len(set(difference_lst)) == 1: #등차수열일때
        hansu_lst.append(num)
print(len(hansu_lst))

