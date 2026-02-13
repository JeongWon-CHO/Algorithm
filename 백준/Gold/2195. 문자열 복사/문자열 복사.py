S = input()
P = input()

cnt = 0
idx = 0
while (idx < len(P)):
  link = [0]

  for j in range(len(S)):
    if P[idx] == S[j]:
      tmp = 0
      for k in range(1, min(len(S)-j, len(P)-idx)): # 뒤만 확인할거다. 바로 안 나오면 바로 탈출
        if P[idx+k] == S[j+k]:
          tmp += 1
        else:
          link.append(tmp)
          break
        link.append(tmp)

  idx += max(link)

  idx += 1
  cnt += 1

print(cnt)