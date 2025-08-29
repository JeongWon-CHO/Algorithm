import sys
input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    N = int(input().rstrip())
    L = sorted(list(map(int, input().rstrip().split())))

    result = []
    for i in range(0, N, 2):
        result.append(L[i])

    idx = N-1 if N % 2 == 0 else N-2
    for i in range(idx, -1, -2):
        result.append(L[i])

    answer = 0
    for i in range(N-1):
        answer = max(abs(result[i] - result[i+1]), answer)

    answer = max(abs(result[-1] - result[0]), answer)
    print(answer)