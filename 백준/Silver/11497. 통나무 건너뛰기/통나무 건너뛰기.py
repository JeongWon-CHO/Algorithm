import sys
input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    N = int(input().rstrip())
    L = sorted(list(map(int, input().rstrip().split())))

    answer = 0
    for i in range(N-2):
        answer = max(abs(L[i]-L[i+2]), answer)

    answer = max(abs(L[N-1]-L[N-2]), abs(L[0]-L[1]), answer)

    print(answer)