N = int(input())

rooms = []
for i in range(N):
    A, B = map(int, input().split())
    rooms.append((A, B))

rooms.sort(key=lambda x: (x[1], x[0]))

cnt = 1
endTime = rooms[0][1]
for i in range(1, N):
    if endTime <= rooms[i][0]:
        endTime = rooms[i][1]
        cnt += 1

print(cnt)