T = int(input())

for _ in range(T):
    n = int(input())

    # 입력 =================================
    sticky = [list(map(int, input().split())) for x in range(2)]
    # =====================================

    dp = [[0] * n for x in range(2)]

    dp[0][0] = sticky[0][0]
    dp[1][0] = sticky[1][0]
    if n == 1:
        print(max(dp[0][0], dp[1][0]))
        continue

    dp[0][1] = sticky[0][1] + sticky[1][0]
    dp[1][1] = sticky[1][1] + sticky[0][0]
    if n == 2:
        print(max(dp[0][1], dp[1][1]))
        continue

    for i in range(2, n):
        dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + sticky[0][i]
        dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + sticky[1][i]

    print(max(dp[0][-1], dp[1][-1]))