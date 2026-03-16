total = int(input())

money = 0
for i in range(9):
  tmp = int(input())
  money += tmp

print(total-money)