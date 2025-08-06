N = int(input())

arr = [int(input()) for _ in range(N)]

i = 0
dp = []
while True:
    if i >= N:
        break

    if i == 0:
        dp.append(arr[0])
        i += 1
        continue
    elif i == 1:
        tmp = max(arr[0]+arr[1], arr[1])
        dp.append(tmp)
        i += 1
        continue
    elif i == 2:
        tmp = max(arr[1]+arr[2], arr[0]+arr[2])
        dp.append(tmp)
        i += 1
        continue

    value = max(dp[i-3] + arr[i-1] + arr[i], dp[i-2] + arr[i])
    dp.append(value)
    i += 1

print(dp[-1])