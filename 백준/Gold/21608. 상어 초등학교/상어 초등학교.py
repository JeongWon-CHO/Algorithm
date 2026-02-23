import sys
input = sys.stdin.readline

N = int(input())

students = [list(map(int, input().rstrip().split())) for _ in range(N*N)]
classRomm = [[0] * N for _ in range(N)]

result = 0
for std in students:
  likes = std[1:]
  
  check = [[0] * N for _ in range(N)]

  for i in range(N):
    for j in range(N):
      if classRomm[i][j] in likes:
        if j-1 >= 0: check[i][j-1] += 1
        if j+1 < N: check[i][j+1] += 1
        if i+1 < N: check[i+1][j] += 1
        if i-1 >= 0: check[i-1][j] += 1
  
  step1 = []
  maxValue = 0
  for i in range(N):
    for j in range(N):
      if classRomm[i][j] != 0:  # 채워진 칸 방지
        continue

      if check[i][j] == maxValue:
        maxValue = check[i][j]
        step1.append((i, j))
        continue

      if check[i][j] > maxValue:
        maxValue = check[i][j]
        step1 = [(i, j)]
        continue
  
  if len(step1) > 1:
    step2 = []

    for x, y in step1:
      cnt = 0
      if x-1 >= 0:
        if classRomm[x-1][y] == 0:
          cnt += 1
      if x+1 < N:
        if classRomm[x+1][y] == 0:
          cnt += 1
      if y-1 >= 0:
        if classRomm[x][y-1] == 0:
          cnt += 1
      if y+1 < N:
        if classRomm[x][y+1] == 0:
          cnt += 1

      step2.append((cnt, x, y))
    

    maxStep2 = []
    maxStep2Value = -1
    for s in step2:
      if s[0] == maxStep2Value:
        maxStep2Value = s[0]
        maxStep2.append((s[1], s[2]))
        continue
      if s[0] > maxStep2Value:
        maxStep2Value = s[0]
        maxStep2 = [(s[1], s[2])]
    
    if len(maxStep2) > 1:
      maxStep2.sort(key=lambda x: (x[0], x[1]))
    
    curY= maxStep2[0][0]
    curX = maxStep2[0][1]
    classRomm[curY][curX] = std[0]

  else:
    curY = step1[0][0]
    curX = step1[0][1]

    classRomm[curY][curX] = std[0]

# 만족도 조사
for s in students:
  target = s[0]
  candi = s[1:]

  for i in range(N):
    flag = False

    for j in range(N):
      if classRomm[i][j] == target:

        love = 0
        if i-1 >= 0:
          if classRomm[i-1][j] in candi: love += 1
        if i+1 < N:
          if classRomm[i+1][j] in candi: love += 1
        if j-1 >= 0:
          if classRomm[i][j-1] in candi: love += 1
        if j+1 < N:
          if classRomm[i][j+1] in candi: love += 1
        

        comfortant = 0
        if love == 0:
          comfortant = 0
        elif love == 1:
          comfortant = 1
        elif love == 2:
          comfortant = 10
        elif love == 3:
          comfortant = 100
        elif love == 4:
          comfortant = 1000
        
        result += comfortant
        flag = True
        break
    if flag:
      break

print(result)