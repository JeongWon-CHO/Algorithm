N = int(input())

arr = list(map(int, input().split()))

dpMax = arr
dpMin = arr

for i in range(1, N):
    arr = list(map(int, input().split()))

    dpMax = [max(dpMax[0], dpMax[1]) + arr[0], max(dpMax[0], dpMax[1], dpMax[2]) + arr[1], max(dpMax[1], dpMax[2]) + arr[2]]
    dpMin = [min(dpMin[0], dpMin[1]) + arr[0], min(dpMin[0], dpMin[1], dpMin[2]) + arr[1], min(dpMin[1], dpMin[2]) + arr[2]]

print(max(dpMax), min(dpMin))