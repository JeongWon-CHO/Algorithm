import sys
input = sys.stdin.readline


N, M, B = map(int, input().rstrip().split())

map = [list(map(int, input().rstrip().split())) for x in range(N)]

max_height = 0
for i in map:
    if max_height < max(i):
        max_height = max(i)

height = max_height
have = B
min_time_height = 0
min_time = 1061109567
for current_height in range(max_height, -1, -1):
    time = 0
    have = B
    for i in range(N):
        for j in range(M):

            if map[i][j] - current_height > 0:  # 블럭을 빼야함 -> 2초
                time += (map[i][j] - current_height) * 2
                have += (map[i][j] - current_height)
            else:  # 블럭을 쌓아야 함 -> 1초
                time += (current_height - map[i][j])
                have -= (current_height - map[i][j])

    if have >= 0:
        if min_time > time:
            min_time_height = current_height
            min_time = time

print(min_time, min_time_height)
