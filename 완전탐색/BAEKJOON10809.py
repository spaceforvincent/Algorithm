word = list(input())#baekjoon
alphabet = []
for i in range(26):
    alphabet.append(chr(i+97)) #a,b,c,d,...z

for i in range(len(alphabet)):
    if alphabet[i] in word:
        alphabet[i] = str(word.index(alphabet[i])) #진작에 이걸 써먹었으면 빨리 풀었을 문제지만...
    else:
        alphabet[i] = '-1'

print(' '.join(alphabet))
