from collections import deque

N, M = map(int, input().split())

arr = [list(input()) for _ in range(N)]

dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]

def ROLLING(y, x, dy, dx):
  cnt = 0
  while arr[y + dy][x + dx] != "#" and arr[y][x] != "O":
    x += dx
    y += dy
    cnt += 1

  return y, x, cnt


def BFS(stRY, stRX, stBY, stBX):
  q = deque()
  visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]

  visited[stRY][stRX][stBY][stBX] = True
  q.append((stRY, stRX, stBY, stBX, 1))

  while q:
    redY, redX, blueY, blueX, cnt = q.popleft()

    if cnt > 10:
      break

    for i in range(4):
      nRy, nRx, cntR = ROLLING(redY, redX, dy[i], dx[i])
      nBy, nBx, cntB = ROLLING(blueY, blueX, dy[i], dx[i])

      if arr[nBy][nBx] == 'O':
        continue

      if arr[nRy][nRx] == 'O':
        return cnt
      
      if nRy == nBy and nRx == nBx:
        if cntR > cntB:
          nRy -= dy[i]
          nRx -= dx[i]
        else:
          nBy -= dy[i]
          nBx -= dx[i]
      
      if not visited[nRy][nRx][nBy][nBx]:
        visited[nRy][nRx][nBy][nBx] = True
        q.append((nRy, nRx, nBy, nBx, cnt + 1))
  
  return -1


redY, redX, blueY, blueX = 0, 0, 0, 0
for i in range(N):
  for j in range(M):
    if arr[i][j] == 'R':
      redY, redX = i, j
    if arr[i][j] == 'B':
      blueY, blueX = i, j

result = BFS(redY, redX, blueY, blueX)
print(result)