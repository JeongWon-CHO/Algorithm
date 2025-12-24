N, M = map(int, input().split())
r, c, d = map(int, input().split())  # 0: 북  |  1: 동  |  2: 남  |  3: 서

arr = [list(map(int, input().split())) for _ in range(N)]

dy = [-1, 0, 1, 0]  # 북 동 남 서
dx = [0, 1, 0, -1]


def OOB(y, x):
    return y < 0 or x < 0 or y >= N or x >= M


count = 0

curY = r
curX = c
curD = d

while True:
    if arr[curY][curX] == 0:  # 현재 칸이 아직 청소되지 않은 경우
        arr[curY][curX] = 2
        count += 1

    # 현재 칸의 주변 4칸 비교
    isMove = False
    for _ in range(4):
        curD = (curD + 3) % 4  # 반시계로 90도 회전
        ny = curY + dy[curD]
        nx = curX + dx[curD]

        if not OOB(ny, nx) and arr[ny][nx] == 0:
            curY, curX = ny, nx
            isMove = True
            break

    if not isMove:  # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
        if OOB(curY - dy[curD], curX - dx[curD]) or arr[curY - dy[curD]][curX - dx[curD]] == 1:
            break  # 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
        else:
            curY = curY - dy[curD]
            curX = curX - dx[curD]

print(count)