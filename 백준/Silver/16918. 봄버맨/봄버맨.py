import sys
input = sys.stdin.readline

R, C, N = map(int, input().rstrip().split())

grid = [list(input().rstrip()) for _ in range(R)]

dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]


def OOB(y, x, n, m):
    return y<0 or x<0 or y>=n or x>=m


bomb = [[-1] * C for _ in range(R)]

# 초기세팅
for i in range(R):
    for j in range(C):
        if grid[i][j] == 'O':
            bomb[i][j] = 0

# 1초는 가만히 있으니까 패스

# 폭탄 시작 (2초 때부터)
for second in range(2, N+1):
    for i in range(R):
        for j in range(C):
            # 폭탄 없는 칸에 다 심기
            if second % 2 == 0:
                if bomb[i][j] == -1:
                    bomb[i][j] = second % 3
            else:  # 폭탄 터치기
                if (second % 3) == bomb[i][j]:
                    if not OOB(i-1, j, R, C):
                        if bomb[i - 1][j] != bomb[i][j]:
                            bomb[i - 1][j] = -1

                    if not OOB(i+1, j, R, C):
                        if bomb[i + 1][j] != bomb[i][j]:
                            bomb[i + 1][j] = -1

                    if not OOB(i, j-1, R, C):
                        if bomb[i][j - 1] != bomb[i][j]:
                            bomb[i][j - 1] = -1

                    if not OOB(i, j+1, R, C):
                        if bomb[i][j + 1] != bomb[i][j]:
                            bomb[i][j + 1] = -1
                    bomb[i][j] = -1


# 출력
for i in range(R):
    for j in range(C):
        if bomb[i][j] != -1:
            print('O', end='')
        else:
            print('.', end='')
    print()