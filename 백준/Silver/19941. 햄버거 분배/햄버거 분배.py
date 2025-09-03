N, K = map(int, input().split())

hamburger = list(input())

cnt = 0
for i in range(N):
    if hamburger[i] == 'P':
        for j in range(i-K, i+K+1):
            if len(hamburger) <= j:
                break

            if j < 0:
                continue

            if hamburger[j] == 'H':
                cnt += 1
                hamburger[j] = '.'  # 먹은 햄버거 표시
                hamburger[i] = '.'  # 먹은 사람 표시
                break

print(cnt)