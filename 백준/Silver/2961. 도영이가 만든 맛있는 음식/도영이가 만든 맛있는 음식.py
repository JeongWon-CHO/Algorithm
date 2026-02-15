from itertools import combinations

N = int(input())
indi = [list(map(int, input().split())) for _ in range(N)]

result = 1000000000
for i in indi:
  result = min(abs(i[1] - i[0]), result)

for i in range(2, N+1):
  cob = list(combinations(indi, i))
  
  for target in cob:
    curS = 1
    curB = 0
    for j in target:
      curS *= j[0]
      curB += j[1]

    result = min(abs(curB-curS), result)

print(result)