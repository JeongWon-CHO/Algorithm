from collections import deque

N, K = map(int, input().split())

q = deque()
q.append(N)

visited = [-1] * 100001
visited[N] = 0

while q:
    x = q.popleft()

    if x == K:
        print(visited[x])
        break

    for i in [x-1, x+1, x*2]:
      if i < 0 or 100000 < i:
        continue
      
      if visited[i] != -1:
        continue
      
      visited[i] = visited[x] + 1
      q.append(i)