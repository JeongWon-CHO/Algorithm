N, M = map(int, input().split())

road = []
for i in range(N):
    length, speed = map(int, input().split())
    for j in range(length):
        road.append(speed)

yeonjeong = []
for i in range(M):
    length, speed = map(int, input().split())
    for j in range(length):
        yeonjeong.append(speed)

max_value = 0
for i in range(100):
    max_value = max(max_value, yeonjeong[i]-road[i])

print(max_value)