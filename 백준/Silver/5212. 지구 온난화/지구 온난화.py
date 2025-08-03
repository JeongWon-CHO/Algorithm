import copy

R, C = map(int, input().split())

grid = [list(input()) for x in range(R)]
newGrid = copy.deepcopy(grid)

dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]


def OOB(y, x, n, m):
    return y < 0 or x < 0 or y >= n or x >= m


for i in range(R):
    for j in range(C):
        if grid[i][j] == "X":
            cnt = 0
            for k in range(4):
                ny = i + dy[k]
                nx = j + dx[k]
                if OOB(ny, nx, R, C) or grid[ny][nx] == ".":
                    cnt += 1
            if cnt >= 3:
                newGrid[i][j] = "."

max_x = -1
max_y = -1
min_x = C
min_y = R

for i in range(R):
    for j in range(C):
        if newGrid[i][j] == "X" and max_x < j:
            max_x = j
        if newGrid[i][j] == "X" and max_y < i:
            max_y = i
        if newGrid[i][j] == "X" and min_x > j:
            min_x = j
        if newGrid[i][j] == "X" and min_y > i:
            min_y = i

for i in range(min_y, max_y+1):
    for j in range(min_x, max_x+1):
        print(newGrid[i][j], end="")

    print()
