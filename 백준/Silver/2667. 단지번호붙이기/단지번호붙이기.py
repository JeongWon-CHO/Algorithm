from collections import deque

N = int(input())

apartment = [list(input()) for _ in range(N)]

dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]


def OOB(y, x):  # 범위 밖에 나갔는지 체크
    return y < 0 or x < 0 or y >= N or x >= N


def BFS(stY, stX, board, target):

    q = deque()
    dist = [[-1] * N for _ in range(N)]

    dist[stY][stX] = 1
    q.append((stY, stX))

    cnt = 1

    while q:
        curY, curX = q.popleft()

        for i in range(4):
            ny = curY + dy[i]
            nx = curX + dx[i]

            if OOB(ny, nx):
                continue
            if dist[ny][nx] != -1:
                continue
            if board[ny][nx] == '0':
                continue

            cnt += 1
            dist[ny][nx] = cnt
            board[ny][nx] = target
            q.append((ny, nx))

    return cnt


t = 0
result = []
for i in range(N):
    for j in range(N):
        if apartment[i][j] == '1':
            t += 1
            result.append(BFS(i, j, apartment, t))
print(t)

result.sort()
for i in result:
    print(i)