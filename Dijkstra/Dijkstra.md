# Dijkstra



- 그래프에서 여러개의 노드가 있을 때, 특정한 노드에서 출발하여 다른 노드로 가는 각각의 최단 경로를 구하는 알고리즘
- 음의 간선이 없을 때 정상적으로 동작한다
- GPS 소프트웨어의 기본 알고리즘
- 기본적으로 그리디 알고리즘으로 분류됨
- 동작 원리
  - 출발 노드 설정
  - 최단 거리 테이블 초기화
  - 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드 선택
  - 해당 노드 거쳐 다른 노드로 가는 비용 계산하여 최단 거리 테이블 갱신
  - 3, 4번 반복
- 최단 경로를 구하는 과정에서 각 노드에 대한 현재까지의 최단거리 정보를 항상 1차원 리스트에 저장
- 매번 현재 처리하고 있는 노드를 기준으로 주변 간선 확인
- 한 단계 당 하나의 노드에 대한 최단 거리를 확실히 찾음



1. 간단한 방식

```
def get_smallest_node(): #방문하지 않은 노드 중에서 가장 최단거리가 짧은 노드 번호 반환
    min_value = 987654321
    index = 0 
    for i in range(1,N+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i #가장 최단 거리가 짧은 노드
     
    return index
 
def dijkstra(s):
    #시작 노드 초기화
    distance[s] = 0
    visited[s] = 1
    for j in graph[s]:
        distance[j[0]] = j[1] #e까지의 거리는 w
    for i in range(N-1):
        #현재 최단 거리 가장 짧은 노드 꺼내서 방문 처리
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
     
    #graph에 간선정보 입력받기
    for i in range(E):
        s, e, w = list(map(int, input().split()))
        graph[s].append((e,w)) #s에서 e로 가는 비용이 w
 
 
    dijkstra(0)
 
    for i in range(1,N+1):
        if not graph[i]: #다음 목적지와 비용이 담겨있지 않다 : 마지막 연결지점이다
            print(f'#{tc} {distance[i]}')
```





2. 개선된 다익스트라 알고리즘

```
def dijkstra(s):
    Q = []
    heapq.heappush(Q,(0,s))
    distance[s] = 0
    while Q:
        #가장 최단거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(Q)
        #이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        #현재 노드와 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            #현재 노드를 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우
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
```

