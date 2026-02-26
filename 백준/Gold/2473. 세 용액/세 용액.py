import sys
input = sys.stdin.readline

N = int(input())

water = list(map(int, input().split()))
water.sort()

minValue = 3000000001
curWater = [-1, -1, -1]
for i in range(N-2):

  left = i+1
  right = N-1
  standard = water[i]

  while left < right:
    result = standard + water[left] + water[right]

    if abs(result) < abs(minValue):
      curWater[0] = standard
      curWater[1] = water[left]
      curWater[2] = water[right]
      minValue = result

    if result > 0:
      right -= 1

    elif result < 0:
      left += 1

    elif result == 0:
      curWater[0] = standard
      curWater[1] = water[left]
      curWater[2] = water[right]
      break

curWater.sort()
print(curWater[0], curWater[1], curWater[2])