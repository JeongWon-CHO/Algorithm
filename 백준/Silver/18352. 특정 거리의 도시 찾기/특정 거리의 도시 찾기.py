import sys

input = sys.stdin.readline

from collections import deque

N, M, K, X = map(int, input().rstrip().split())

graph = [[] for x in range(N+1)]

for i in range(M):
    A, B = map(int, input().rstrip().split())
    graph[A].append(B)

dist = [-1] * (N+1)
q = deque()

dist[X] = 0
q.append(X)

while q:
    curX = q.popleft()

    for k in graph[curX]:
        if dist[k] != -1:
            continue

        dist[k] = dist[curX] + 1
        q.append(k)

check = True
for i in range(len(dist)):
    if dist[i] == K:
        print(i)
        check = False

if check:
    print(-1)