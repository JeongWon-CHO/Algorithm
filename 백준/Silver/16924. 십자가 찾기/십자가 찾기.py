import copy
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

grid = [list(input().rstrip()) for x in range(N)]


check_gird = copy.deepcopy(grid)
# print(check_gird)

cnt = 0
shipZaGa = []


def OOB(x, y):
    return y < 0 or x < 0 or x >= N or y >= M


for x in range(N):
    for y in range(M):
        size = 0

        if grid[x][y] == '*':
            for i in range(1, N):  # 고무고무!
                if OOB(x+i, y) or OOB(x-i, y) or OOB(x, y+i) or OOB(x, y-i): break

                if grid[x+i][y] == '*' and grid[x-i][y] == '*' and grid[x][y+i] == '*' and grid[x][y-i] == '*':
                    size += 1
                    check_gird[x][y] = '.'
                    check_gird[x][y-i] = '.'
                    check_gird[x][y+i] = '.'
                    check_gird[x-i][y] = '.'
                    check_gird[x+i][y] = '.'
                    shipZaGa.append([x + 1, y + 1, size])
                else:
                    break
        else:
            continue


# print(check_gird)

isPossible = True
for i in range(N):
    for j in range(M):
        if check_gird[i][j] == '*':
            isPossible = False
            break

if isPossible:
    print(len(shipZaGa))
    for i in shipZaGa:
        print(i[0], i[1], i[2])
else:
    print(-1)
