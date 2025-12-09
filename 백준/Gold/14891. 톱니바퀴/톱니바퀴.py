from  collections import deque
wheel = []

for _ in range(4):
    wheel.append(deque(list(input())))

K = int(input())
R = [list(map(int, input().split())) for _ in range(K)]


def left(num, direction):
    if num < 0:
        return
    if wheel[num][2] != wheel[num+1][6]:
        left(num-1, -direction)
        wheel[num].rotate(direction)


def right(num, direction):
    if num > 3:
        return
    if wheel[num][6] != wheel[num-1][2]:
        right(num+1, -direction)
        wheel[num].rotate(direction)


for i in range(K):
    target = R[i][0] - 1
    direction = R[i][1]

    left(target - 1, -direction)
    right(target + 1, -direction)
    wheel[target].rotate(direction)

result = 0

if wheel[0][0] == '1':
    result += 1
if wheel[1][0] == '1':
    result += 2
if wheel[2][0] == '1':
    result += 4
if wheel[3][0] == '1':
    result += 8

print(result)
