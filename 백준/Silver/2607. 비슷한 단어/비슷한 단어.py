import sys
input = sys.stdin.readline

N = int(input().rstrip())
word = input().rstrip()

target = [input().rstrip() for _ in range(N-1)]
wordDict = {chr(x): 0 for x in range(65, 91)}

# 기준 문자열 카운트
for i in range(len(word)):
    wordDict[word[i]] += 1

cnt = 0
for i in target:
    targetDict = {chr(x): 0 for x in range(65, 91)}

    for j in range(len(i)):
        targetDict[i[j]] += 1

    differentCnt = 0
    for k in wordDict:
        if abs(wordDict[k] - targetDict[k]) > 0:
            differentCnt += abs(wordDict[k] - targetDict[k])

    if len(i) == len(word):
        if differentCnt <= 2:
            cnt += 1
    else:
        if differentCnt <= 1:
            cnt += 1

print(cnt)