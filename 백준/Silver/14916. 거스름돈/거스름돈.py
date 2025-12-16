n = int(input())

if n == 1 or n == 3:
    print(-1)
elif n == 2:
    print(1)
elif n == 4:
    print(2)
elif n == 5:
    print(1)
else:
    dp = [100000] * (n + 1)
    dp[2] = 1
    dp[4] = 2
    dp[5] = 1

    for i in range(6, n+1):
        dp[i] = min(dp[i], dp[i-2]+1, dp[i-5]+1)

    print(dp[-1])