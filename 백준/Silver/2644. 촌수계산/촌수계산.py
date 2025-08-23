from collections import deque
import sys
input = sys.stdin.readline

N = int(input().rstrip())
start, end = map(int, input().rstrip().split())
M = int(input().rstrip())

family = [[] for _ in range(N+1)]

for i in range(M):
    parent, child = map(int, input().split())
    family[parent].append(child)
    family[child].append(parent)

q = deque()
dist = [-1] * (N+1)

dist[start] = 0
q.append(start)

while q:
    cur = q.popleft()

    for i in family[cur]:
        if dist[i] != -1:
            continue

        dist[i] = dist[cur] + 1
        q.append(i)

print(dist[end])