### BFS

- 가까운 노드부터 탐색하는 알고리즘
- 미로/경로 찾기의 전형적인 template
- 큐 자료구조를 이용하는 것이 정석
- 동작 과정
  - 탐색 시작 노드를 큐에 삽입하고 방문처리
  - 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리
  - 2번의 과정을 더 이상 수행할 수 없을 때까지 반복
  - enQue : 방문할 정점 등록, deQue : 방문
- 일반적인 경우 실제 수행 시간은 DFS보다 좋은 편

```python
from collections import deque

def BFS(graph, v, visited):
    Q = deque(v)
    
    #현재 노드 방문 처리
    visited[v] = True
    
    #큐가 빌 때까지 반복
    while Q:
        #큐에서 하나의 원소 뽑아 출력 (정점 방문)
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



