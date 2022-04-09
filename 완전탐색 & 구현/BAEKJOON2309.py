#일곱난쟁이
import sys
from itertools import combinations


arr = []
for i in range(9):
    arr.append(int(sys.stdin.readline()))

for i in combinations(arr, 7):
    if sum(i) == 100:
        ans = sorted(i)

for j in range(len(ans)):
    print(ans[j])


