import sys
from itertools import  permutations
N = int(sys.stdin.readline().rstrip())

nums = list(permutations(["1", "2", "3", "4", "5", "6", "7", "8", "9"], 3))

for _ in range(N):

    minHyeck, strike, ball = map(int, sys.stdin.readline().rstrip().split())
    delete = 0
    minStr = list(str(minHyeck))

    for i in range(len(nums)):
        strikeCnt = 0
        ballCnt = 0
        i -= delete

        for j in range(3):
            if nums[i][j] == minStr[j]:
                strikeCnt += 1
            elif minStr[j] in nums[i]:
                ballCnt += 1

        if (strikeCnt != strike) or (ballCnt != ball):
            nums.remove(nums[i])
            delete += 1

print(len(nums))