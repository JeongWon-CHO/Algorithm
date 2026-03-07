import sys
input = sys.stdin.readline

N, M = map(int, input().split())

num = list(map(int, input().split()))

dp = [0] * (N+1)
dp[1] = num[0]
for i in range(2, N+1):
  dp[i] = dp[i-1] + num[i-1]

for _ in range(M):
  a, b = map(int, input().split())

  print(dp[b] - dp[a-1])