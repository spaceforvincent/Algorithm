#단어 수학
import sys
from copy import deepcopy

N = int(sys.stdin.readline())
lst = []
for i in range(N):
    lst.append(sys.stdin.readline().rstrip())

lst = sorted(lst, key = len) #더 자릿수가 큰 숫자가 뒤로 오게 정렬(중복 경우 위해)

for i in range(len(lst)):
    lst[i] = list(map(str, lst[i])) #숫자별로 한 알파벳씩 분리

lst2 = deepcopy(lst) #조작용 리스트 복사

dic = {}
for i in range(len(lst)):
    for j in range(len(lst[i])):
        dic[lst2[i][0]] = [len(lst2[i]), j] #정렬 위한 전처리(자릿수, 알파벳이 그 숫자에서 몇번째 있는지)
        lst2[i].pop(0)

lst2 = list(map(list, sorted(dic.items(), key = lambda x: -x[1][0]))) #우선순위 : 자릿수 -> 인덱스

for i in range(0, len(lst2)):
    lst2[i][1] = 9 - i
    dic[lst2[i][0]] = lst2[i][1] #정렬된 순서대로 9부터 차례로 순서배정

for i in range(len(lst)):
    for j in range(len(lst[i])):
        lst[i][j] = str(dic[lst[i][j]]) #조인을 위한 str형변환
    lst[i] = ''.join(lst[i])

lst = list(map(int, lst))
print(sum(lst))
