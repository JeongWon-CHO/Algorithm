from collections import deque

N, M = map(int, input().split()) # R  /  C

maze = [list(input()) for _ in range(N)]

dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]

def OOB(y, x):
  return y < 0 or x < 0 or y >= N or x >= M


def isExit(y, x):  # 여기가 출구인지 확인 (출구면 True)  
  return y <= 0 or x <= 0 or  y+1 >= N or x+1 >= M


def BFS(stY, stX, board, dist):

  q = deque()

  dist[stY][stX] = 0

  q.append((stY, stX))

  while q:
    curY, curX = q.popleft()

    if isExit(curY, curX):
      return dist[curY][curX] + 1

    if board[curY][curX] == '.':  # 탈출 가능성이 보인다면..
        if isExit(curY, curX):
          return dist[curY][curX]

    for i in range(4):
      ny = curY + dy[i]
      nx = curX + dx[i]

      if OOB(ny, nx):
        continue
      elif dist[ny][nx] != -1:
        continue
      elif board[ny][nx] == '#':
        continue
      elif board[ny][nx] == 'F':
        continue
      elif fireDist[ny][nx] <= dist[curY][curX] + 1 and fireDist[ny][nx] != -1:  # 불이 지나갈 자리인지 파악
        continue
      
      dist[ny][nx] = dist[curY][curX] + 1
      q.append((ny, nx))
  
  return -1


def FIREBFS(stY, stX, board, fireDist):
  
  q = deque()

  fireDist[stY][stX] = 0

  q.append((stY, stX))

  while q:
    curY, curX = q.popleft()

    for i in range(4):
      ny = curY + dy[i]
      nx = curX + dx[i]

      if OOB(ny, nx):
        continue
      elif fireDist[ny][nx] != -1:
        if fireDist[ny][nx] <= fireDist[curY][curX] + 1:
          continue
      elif board[ny][nx] == '#':
        continue
      elif board[ny][nx] == 'F':
        continue
      
      fireDist[ny][nx] = fireDist[curY][curX] + 1
      q.append((ny, nx))
  
  return -1

dist = [[-1] * M for _ in range(N)]
fireDist = [[-1] * M for _ in range(N)]

result = -1
# Fire 돌리기
for i in range(N):
  for j in range(M):
    if maze[i][j] == 'F':
      fireResult = FIREBFS(i, j, maze, fireDist)

# 사람 돌리기
for i in range(N):
  for j in range(M):
    if maze[i][j] == 'J':
      result = BFS(i, j, maze, dist)

    if maze[i][j] == 'F':
      fireResult = BFS(i, j, maze, fireDist)

if result == -1:
  print('IMPOSSIBLE')
else:
  print(result)