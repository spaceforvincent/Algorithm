#숫자카드 2

def lowerBound(target):
    start = 0
    end = N
    while start < end:  
        mid = (start+end)//2
        if target <= lst[mid]:
            end = mid
        else:
            start = mid+1
    return end


def upperBound(target):
    start = 0
    end = N
    while start < end:
        mid = (start+end)//2
        if target < lst[mid]:
            end = mid
        else:
            start = mid+1
    return end

import sys

N = int(sys.stdin.readline())
lst = sorted(list(map(int, sys.stdin.readline().split())))

find = int(sys.stdin.readline())
find_lst = list(map(int, sys.stdin.readline().split()))


for i in find_lst:
    print(upperBound(i)-lowerBound(i), end=' ')