from collections import deque

N, K = map(int, input().split())

examiner = [list(map(int, input().split())) for _ in range(N)]

S, X, Y = map(int, input().split())  # 초, X, Y

dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]


def OOB(y, x):
    return y<0 or x<0 or y>=N or x>=N


def BFS(s, board):
    n = len(board)
    m = len(board[0])

    q = deque()
    dist = [[-1] * m for _ in range(n)]

    for target in range(1, K+1):
        for y in range(N):
            for x in range(N):
                if examiner[y][x] == target:
                    q.append((y, x))
                    dist[y][x] = 0

    while q:
        curY, curX = q.popleft()

        if dist[curY][curX] == s:
            break

        for i in range(4):
            ny = curY + dy[i]
            nx = curX + dx[i]

            if OOB(ny, nx):
                continue
            if dist[ny][nx] != -1:
                continue

            dist[ny][nx] = dist[curY][curX] + 1
            board[ny][nx] = board[curY][curX]

            q.append((ny, nx))


BFS(S, examiner)
print(examiner[X-1][Y-1])