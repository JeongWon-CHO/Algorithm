import sys
from collections import deque
input = sys.stdin.readline


dy = [1, 2, 2, 1, -1, -2, -2, -1]
dx = [-2, -1, 1, 2, 2, 1, -1, -2]


def bfs(stY, stX, board, size, goalX, goalY):
    q = deque()
    dist = [[-1] * size for _ in range(size)]

    q.append((stY, stX))
    dist[stY][stX] = 0

    while q:
        cur_y, cur_x = q.popleft()

        if cur_y == goalY and cur_x == goalX:
            return dist[cur_y][cur_x]

        # 8방향 탐색
        for i in range(8):
            ny = cur_y + dy[i]
            nx = cur_x + dx[i]

            if ny < 0 or nx < 0 or ny >= size or nx >= size:
                continue
            if dist[ny][nx] != -1:
                continue

            dist[ny][nx] = dist[cur_y][cur_x] + 1
            q.append((ny, nx))

    return dist[goalY][goalX]


T = int(input().rstrip())

for i in range(T):
    I = int(input().rstrip())  # 체스판 크기
    current_x, current_y = map(int, input().rstrip().split())  # 현재 있는 칸 (0 0)
    goal_x, goal_y = map(int, input().rstrip().split())  # 이동 하려는 칸 (7 0)

    chess = [0 for _ in range(I)]
    size = I
    result = bfs(current_y, current_x, chess, I, goal_x, goal_y)

    print(result)
