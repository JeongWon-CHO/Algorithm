N = int(input())

timeTable = []
for i in range(1, N+1):
    T, S = map(int, input().split())
    timeTable.append([T, S])

timeTable.sort(key=lambda x:x[1], reverse=True)

schedule = [0] * 24

currentTime = timeTable[0][1] - timeTable[0][0]
for t, s in timeTable[1:]:
    if currentTime > s:
        currentTime = s - t
    else:
        currentTime -= t

if currentTime > 0:
    print(currentTime)
else:
    print(-1)