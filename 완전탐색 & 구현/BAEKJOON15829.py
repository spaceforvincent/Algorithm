#해싱
import sys
t = int(sys.stdin.readline())
st = list(sys.stdin.readline().rstrip())

lst = []
for i in range(len(st)):
    lst.append((ord(st[i]) - 96) * (31 ** i)) 

print(sum(lst) % 1234567891)