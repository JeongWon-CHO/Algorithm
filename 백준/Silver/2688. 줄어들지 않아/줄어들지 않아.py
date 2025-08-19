import sys
input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    N = int(input().rstrip())

    dp = [1 for x in range(10)]

    for i in range(N-1):
        for j in range(9):
            dp[j] = sum(dp[j:])

    print(sum(dp))
