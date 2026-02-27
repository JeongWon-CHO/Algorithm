import sys
input = sys.stdin.readline

N = int(input())

result = [i for i in range(1, N+1)]

predict = []

for i in range(1, N+1):
  tmp = int(input())
  predict.append(tmp)

predict.sort()

bad = 0
for i in range(N):
  bad += abs(predict[i] - result[i])

print(bad)