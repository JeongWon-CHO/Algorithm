from collections import deque

dy = [2, 1, -1, -2, -2, -1, 1, 2]
dx = [1, 2, 2, 1, -1, -2, -2, -1]


def OOB(y, x):
    return y < 0 or x < 0 or y >= N or x >= N


def bfs(stY, stX, board, N):
    q = deque()
    dist = [[-1] * N for _ in range(N)]

    q.append((stY, stX))
    dist[stY][stX] = 0

    while q:
        cur_y, cur_x = q.popleft()

        for i in range(8):
            ny = cur_y + dy[i]
            nx = cur_x + dx[i]

            if OOB(ny, nx):
                continue
            if dist[ny][nx] != -1:
                continue

            dist[ny][nx] = dist[cur_y][cur_x] + 1
            q.append((ny, nx))

    return dist


# N= 체스판 크기   M= 말 갯수
N, M = map(int, input().split())
Y, X = map(int, input().split())

pos = [list(map(int, input().split())) for _ in range(M)]
board = [[0] * N for _ in range(N)]


result = bfs(Y-1, X-1, board, N)

for x, y in pos:
    print(result[x-1][y-1])
