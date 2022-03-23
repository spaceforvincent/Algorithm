import sys
sys.stdin = open('swea4871_input.txt')

def link_recursive(now,visited):
    visited[now] = 1 #방문한 노드는 1로 기록

    for i in draw: #간선 리스트 돌면서
        if visited[i[0]] == 1: #방문했던 곳은 스킵
            continue

        if i[1] == now: #간선 그린 정보 중에 도착지가 now였던 경우의
            link_recursive(i[0],visited) #출발지가 도착지였던 경우를 재귀
             
         
T = int(input())
for tc in range(1,T+1):
    N, L = map(int, input().split()) #노드 개수와 간선 개수
    visited = [0] * (N+1) #방문기록 담는 리스트
    draw = [0] * L
    
    for i in range(L): #간선 그리기
        N1,N2 = map(int, input().split())
        draw[i] = [N1,N2] #draw에 간선 그린 정보 담기 
        
    check1, check2 = map(int, input().split()) #경로의 존재 확인할 출발 노드와 도착 노드
    
    link_recursive(check2 ,visited)
    print(f'#{tc} {visited[check1]}')