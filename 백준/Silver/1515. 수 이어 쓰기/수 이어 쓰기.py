import sys
input = sys.stdin.readline

number = list(input().rstrip())

N = 1  # 현재 예측 수
curIdx = 0  # number 에서 비교 중인 수
while curIdx < len(number):
    tmp = str(N)

    for i in range(len(tmp)):
        if curIdx >= len(number):
            break

        if tmp[i] == number[curIdx]:
            curIdx += 1

    N += 1

print(N-1)