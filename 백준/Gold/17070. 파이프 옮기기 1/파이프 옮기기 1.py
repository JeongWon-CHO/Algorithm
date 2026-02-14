from collections import deque
import sys
input = sys.stdin.readline

N = int(input().rstrip())

room = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0] * 3 for i in range(N)] for _ in range(N)]

dp[0][1][0] = 1  # y, x, dir(0=가로 1=세로 2=대각선)

for i in range(2, N):
  if room[0][i] == 0:
    dp[0][i][0] = dp[0][i-1][0]

for i in range(1, N):
  for j in range(2, N):
    if room[i][j] == 0 and room[i-1][j] == 0 and room[i][j-1] == 0:
      dp[i][j][2] = dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2]
    
    if room[i][j] == 0:
      dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][2]
      dp[i][j][1] = dp[i-1][j][1] + dp[i-1][j][2]

print(dp[N-1][N-1][0] + dp[N-1][N-1][1] + dp[N-1][N-1][2])