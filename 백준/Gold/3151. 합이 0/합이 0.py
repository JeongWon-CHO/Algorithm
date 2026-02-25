from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
A.sort()

cnt = 0

for i in range(N-1):
  for j in range(i+1, N):
    k = (A[i] + A[j]) * -1
    left = bisect_left(A, k, i+1, j)
    right = bisect_right(A, k, i+1, j)
    cnt += right - left

print(cnt)