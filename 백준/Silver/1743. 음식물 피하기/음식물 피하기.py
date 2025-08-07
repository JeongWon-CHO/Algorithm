from collections import deque

N, M, K = map(int, input().split())

grid = [[0] * M for i in range(N)]


for i in range(K):
    x, y = map(int, input().split())
    grid[x-1][y-1] = 1


dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]


def OOB(y, x):
    return y<0 or x<0 or y>=N or x>=M


def check(stY, stX, grid):
    q = deque()

    q.append((stY, stX))
    grid[stY][stX] = 0
    cnt = 0
    while q:
        cur_y, cur_x = q.popleft()

        for i in range(4):
            ny = cur_y + dy[i]
            nx = cur_x + dx[i]

            if OOB(ny, nx):
                continue
            if grid[ny][nx] != 1:
                continue
            if grid[ny][nx] == 0:
                continue

            cnt += 1
            grid[ny][nx] = 0
            q.append((ny, nx))

    return cnt+1


tmp = []
for i in range(N):
    for j in range(M):
        if grid[i][j] == 1:
            count = check(i, j, grid)
            tmp.append(count)

print(max(tmp))
