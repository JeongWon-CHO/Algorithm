D, K = map(int, input().split())

dp = [[0, 0] for _ in range(D)]

dp[0][0] = 1
dp[1][1] = 1
dp[2][0] = 1
dp[2][1] = 1

for i in range(3, D):
    dp[i][0] = dp[i-1][0] + dp[i-2][0]
    dp[i][1] = dp[i-1][1] + dp[i-2][1]


target = 1
while True:
    A = target

    if (K - A*dp[-1][0]) % dp[-1][1] == 0:
        print(A)
        print(int((K - A*dp[-1][0]) / dp[-1][1]))
        break

    target += 1