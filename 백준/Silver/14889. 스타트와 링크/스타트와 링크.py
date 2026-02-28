from itertools import combinations

import sys
input = sys.stdin.readline

N = int(input())
A = [i for i in range(1, N+1)]  # 조합을 위한 배열

player = [list(map(int, input().split())) for _ in range(N)]

starts = list(combinations(A, N//2))

result = 101
for idx in range(len(starts) // 2):
  link = []
  
  for a in A:
    if a not in starts[idx]:
      link.append(a)

  teamWorkOfStarts = 0
  teamWorkOfLinks = 0
  for i in range(N//2):
    for j in range(N//2):

      if starts[idx][i] != starts[idx][j]:
        teamWorkOfStarts += player[starts[idx][i]-1][starts[idx][j]-1]

      if link[i] != link[j]:
        teamWorkOfLinks += player[link[i]-1][link[j]-1]
  
  result = min(result, abs(teamWorkOfLinks-teamWorkOfStarts))

print(result)