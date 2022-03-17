def enq(item):
    global last
    last += 1
    tree[last] = item

    c = last
    p = last // 2

    while p and tree[p] < tree[c]:
        tree[p], tree[c] = tree[c], tree[p]
        c = p
        p = c // 2

def deq():
    global last
    tmp = tree[1]
    tree[1] = tree[last]
    last -= 1

    p = 1
    c = p * 2   # 왼쪽자식
    while c <= last:
        # 오른쪽 자식이 있으면 왼쪽하고 오른쪽하고 비교해서 대표자식 선정
        if c + 1 <= last and tree[c] < tree[c+1]:
            c = c + 1
        if tree[p] < tree[c]: # 부모와 자식 비교
            tree[p], tree[c] = tree[c], tree[p]
            p = c
            c = p * 2
        else:
            break
    return tmp


# 최대힙
last = 0 # 힙의 원소의 개수
tree = [0] * (100)
enq(4)
enq(15)
enq(13)
enq(11)
enq(19)
enq(20)
enq(23)
deq()
print(tree)
