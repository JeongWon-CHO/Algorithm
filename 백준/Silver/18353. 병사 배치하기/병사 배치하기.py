import sys
input = sys.stdin.readline

N = int(input())
killer = list(map(int, input().split()))
killer.reverse()

dp = [1] * N

for i in range(1, N):
  for j in range(i):
    if killer[j] < killer[i]:
      dp[i] = max(dp[i], dp[j]+1)

print(N - max(dp))