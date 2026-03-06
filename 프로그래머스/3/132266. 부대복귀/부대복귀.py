from collections import deque

def solution(n, roads, sources, destination):
    answer = []
    
    # 인접 그래프 만들기
    graph = [[] for _ in range(n+1)]
    
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)
        
    # BFS 탐색
    q = deque()
    dist = [-1] * (n+1)
    
    dist[destination] = 0
    q.append(destination)
    
    while q:
        curX = q.popleft()
        
        for i in graph[curX]:
            if dist[i] != -1:
                continue
                
            dist[i] = dist[curX] + 1
            q.append(i)
    
    
    return [dist[i] for i in sources]