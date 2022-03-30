#ATM

import sys
N = int(sys.stdin.readline())
line = sorted(list(map(int, sys.stdin.readline().split())))
time_line = [0] * N

cum_sum = line[0]
for i in range(len(line)):
    time_line[i] = sum(line[:i+1])

print(sum(time_line))