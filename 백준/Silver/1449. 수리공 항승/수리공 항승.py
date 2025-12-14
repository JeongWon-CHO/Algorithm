N, L = map(int, input().split())

location = sorted(list(map(int, input().split())))

curL = 0
result = 1
for i in range(N):
    if i == 0:
        curL += 1
        continue

    if curL + location[i] - location[i-1] <= L:
        curL += location[i] - location[i-1]
    else:
        curL = 1
        result += 1

print(result)
