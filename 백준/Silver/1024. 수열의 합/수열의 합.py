N, L = map(int, input().split())

for L2 in range(L, 101):
  temp = N - (L2 * (L2 - 1)) // 2

  if temp < 0:
      print(-1)
      break

  if temp % L2 == 0:
      x = temp // L2
      print(* range(x, x + L2))
      break
else:
  print(-1)