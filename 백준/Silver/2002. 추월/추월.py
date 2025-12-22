N = int(input())

entry = dict()
for i in range(N):
    entry[input()] = i

out = [(i, input()) for i in range(N)]

cnt = 0
for i in range(N):
    for j in range(i+1, N):
        if entry[out[i][1]] > entry[out[j][1]]:
            cnt += 1
            break

print(cnt)