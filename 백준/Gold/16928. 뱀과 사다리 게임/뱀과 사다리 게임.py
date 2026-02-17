from collections import deque

N, M = map(int, input().split())

board = [i for i in range(101)]

def BFS(stX):

  q = deque()
  dist = [-1] * 101

  dist[stX] = 0
  q.append(stX)

  while q:
    curX = q.popleft()

    for i in range(1, 7):
      nx = curX + i

      if nx > 100:
        continue

      move = board[nx]  # 사다리나 뱀 있으면 반영

      if dist[move] != -1:
        continue

      dist[move] = dist[curX] + 1
      if move == 100:
        return dist

      q.append(move)


for i in range(N+M):
  x, y = map(int, input().split())
  board[x] = y

result = BFS(1)

print(result[100])