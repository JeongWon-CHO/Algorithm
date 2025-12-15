from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]


def OOB(y, x, n, m):
    return y < 0 or x < 0 or y >= n or x >= m


def BFS(stY, stX, board):
    n = len(board)
    m = len(board[0])

    q = deque()
    dist = [[-1] * m for _ in range(n)]

    q.append((stY, stX))
    dist[stY][stX] = 0

    sheep = 0
    wolf = 0

    while q:
        cur_y, cur_x = q.popleft()

        for i in range(4):
            ny = cur_y + dy[i]
            nx = cur_x + dx[i]

            if OOB(ny, nx, n, m):
                continue
            if dist[ny][nx] != -1:
                continue
            if board[ny][nx] == '#':
                continue

            if board[ny][nx] == 'o':
                sheep += 1
            elif board[ny][nx] == 'v':
                wolf += 1

            board[ny][nx] = 'e'  # 지나온 길 표시
            dist[ny][nx] = dist[cur_y][cur_x] + 1
            q.append((ny, nx))

    return [sheep, wolf]


R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]

sheep = 0
wolf = 0
for i in range(R):
    for j in range(C):
        if arr[i][j] == 'v':
            tmp_sheep, tmp_wolf = BFS(i, j, arr)

            if tmp_sheep <= tmp_wolf + 1:
                wolf += tmp_wolf + 1
            else:
                sheep += tmp_sheep

        elif arr[i][j] == 'o':
            tmp_sheep, tmp_wolf = BFS(i, j, arr)

            if tmp_sheep + 1 <= tmp_wolf:
                wolf += tmp_wolf
            else:
                sheep += tmp_sheep + 1

print(sheep, wolf)