N = int(input())
scv = list(map(int, input().split()))
scv += [0] * (3 - len(scv))

dp = [[[0] * 61 for i in range(61)] for j in range(61)]
dp[scv[0]][scv[1]][scv[2]] = 1

possible = [(9, 3, 1), (9, 1, 3), (3, 9, 1), (3, 1, 9), (1, 9, 3), (1, 3, 9)]

for i in range(60, -1, -1):
  for j in range(60, -1, -1):
    for k in range(60, -1, -1):
      if dp[i][j][k] > 0:
        for p in possible:
          tmp_i = i - p[0] if i-p[0] >= 0 else 0
          tmp_j = j - p[1] if j-p[1] >= 0 else 0
          tmp_k = k - p[2] if k-p[2] >= 0 else 0

          if dp[tmp_i][tmp_j][tmp_k] == 0 or dp[tmp_i][tmp_j][tmp_k] > dp[i][j][k]+1:
            dp[tmp_i][tmp_j][tmp_k] = dp[i][j][k]+1

print(dp[0][0][0] -1)