#최소 이동 거리

#1. bfs 시도(7/10 맞고 시간초과)

from collections import deque

def bfs(v):
    global ans
    Q = deque()
    Q.append(v)
    visited[v[0][0]][v[0][1]] = v[1]
    while Q:
        v, weight = Q.popleft()
        if v[1] == N:
            if ans > weight:
                ans = weight
        for l in line:
            if l[1] < ans and l[0][0] == v[1] and not visited[l[0][0]][l[0][1]]:
                Q.append((l[0],weight + l[1]))
                visited[l[0][0]][l[0][1]] = weight + l[1]
            elif l[1] < ans and l[0][0] == v[0] and not visited[l[0][0]][l[0][1]]:
                Q.append((l[0],l[1]))
                visited[l[0][0]][l[0][1]] = l[1]

T = int(input())
for tc in range(1,T+1):
    N, E = map(int, input().split())
    visited = [[0] * (N+1) for i in range (N+1)]
    ans = 987654321
    line = []
    for i in range(E):
        s, e, w = list(map(int, input().split()))
        line.append([(s,e),w])
    
    bfs(line[0])
    print(f'#{tc} {ans}')

#2. 다익스트라

def get_smallest_node():
    min_value = 987654321
    index = 0 #가장 최단 거리가 짧은 노드 
    for i in range(1,N+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    
    return index

def dijkstra(s):
    #시작 노드 초기화
    distance[s] = 0
    visited[s] = 1
    for j in graph[s]:
        distance[j[0]] = j[1]
    for i in range(N-1):
        now = get_smallest_node()
        visited[now] = 1
        #현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            #현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost


T = int(input())
for tc in range(1,T+1):
    N, E = map(int, input().split()) #마지막 연결지점 번호, 간선 개수
    visited = [0] * (N+1)
    #각 노드에 연결되어 있는 노드에 대한 정보 담는 리스트 만들기
    graph = [[] for i in range(N+1)]
    #최단거리 테이블을 모두 무한으로 초기화
    distance = [987654321] * (N+1)
    line = []
    for i in range(E):
        s, e, w = list(map(int, input().split()))
        graph[s].append((e,w))


    dijkstra(0)

    for i in range(1,N+1):
        if not graph[i]:
            print(f'#{tc} {distance[i]}')


#3. 개선된 다익스트라(힙큐 사용)

def dijkstra(s):
    Q = []
    heapq.heappush(Q,(0,s))
    distance[s] = 0
    while Q:
        dist, now = heapq.heappop(Q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance [i[0]] = cost
                heapq.heappush(Q, (cost,i[0]))

import heapq

T = int(input())
for tc in range(1,T+1):
    N, E = map(int, input().split()) #마지막 연결지점 번호, 간선 개수
    #각 노드에 연결되어 있는 노드에 대한 정보 담는 리스트 만들기
    graph = [[] for i in range(N+1)]
    #최단거리 테이블을 모두 무한으로 초기화
    distance = [987654321] * (N+1)
    #간선정보 입력받기
    line = []
    for i in range(E):
        s, e, w = list(map(int, input().split()))
        graph[s].append((e,w))


    dijkstra(0)

    for i in range(1,N+1):
        if not graph[i]:
            print(f'#{tc} {distance[i]}')