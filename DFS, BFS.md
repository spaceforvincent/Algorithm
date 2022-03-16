# DFS, BFS



- 스택 : FILO, LIFO
- 큐 : FIFO



 ### 재귀

- 자기자신을 다시 호출
- 종료 조건을 꼭 명시해야 한다.
- 내부적으로 스택 자료구조와 동일 
  - 스택 자료구조를 활용해야 하는 상당수 알고리즘은 재귀함수 이용하면 간편



### DFS

- 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘

  (최대한 멀리 있는 노드를 우선으로 탐색하는 방식으로 동작)

  - 그래프의 구조
    - 노드(정점)
    - 간선 : 두 노드가 간선으로 연결되어 있다면 ''두 노드는 인접하다''라고 표현
  - 인접행렬 : 2차원 배열로 그래프의 연결관계를 표현하는 방식 (메모리 비효율적 BUT 속도 빠름)
  - 인접 리스트 : 리스트로 그래프의 연결 관계를 표현하는 방식 (메모리 효율적 BUT 속도 느림)

  

- 동작과정

  - 탐색 시작 노드를 스택에 삽입하고 방문처리

  - 현재 스택 최상단에 있는 노드에, 방문하지 않은 인접노드가 있으면 그 인접노드를 스택에 넣고 방문처리

    (방문하지 않은 인접노드가 없으면 스택에서 최상단 노드를 꺼냄) 

  - 2번의 과정을 더 이상 수행할 수 없을 때까지 반복



```python
def DFS(graph,v,visited):
    #현재 노드를 방문처리
    visited[v] = True
    
    #해야할 일 처리
    print(v, end=' ')
    
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[v]:
            dfs(graph,i,visited)
            
#인접리스트생성
#visited 배열 생성
#정의된 DFS 함수 호출
```





### BFS

- 가까운 노드부터 탐색하는 알고리즘
- 큐 자료구조를 이용하는 것이 정석
- 동작 과정
  - 탐색 시작 노드를 큐에 삽입하고 방문처리
  - 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리
  - 2번의 과정을 더 이상 수행할 수 없을 때까지 반복
- 일반적인 경우 실제 수행 시간은 DFS보다 좋은 편

```python
from collections import deque

def BFS(graph, v, visited):
    Q = deque(v)
    
    #현재 노드 방문 처리
    visited[v] = True
    
    #큐가 빌 때까지 반복
    while Q:
        #큐에서 하나의 원소 뽑아 출력
        v = Q.popleft()
        #하고 싶은 일 처리
        print(v, end = '')
        #해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if visited[i] == 0:
            	Q.append(i)
                visited[i] = True
                
 
#인접리스트생성
#visited 배열 생성
#정의된 BFS 함수 호출   
```





### 2차원의 탐색문제를 만나면 그래프 형태로 바꿔서 생각한 다음 풀이법을 고민하자
