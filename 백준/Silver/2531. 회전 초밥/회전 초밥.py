import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().rstrip().split())

sushi = [int(input().rstrip()) for _ in range(N)]

result = 0
for i in range(N):
    if i+k > N:
        tmp = len(set(sushi[i:N] + sushi[:(i+k)%N] + [c]))
    else:
        tmp = len(set(sushi[i:i+k] + [c]))

    result = max(result, tmp)

print(result)
