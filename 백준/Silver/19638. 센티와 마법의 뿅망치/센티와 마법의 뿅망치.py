from queue import PriorityQueue
import sys
input = sys.stdin.readline

N, H, T = map(int, input().rstrip().split())

que = PriorityQueue(maxsize=N)

for _ in range(N):
    tmp = int(input().rstrip())
    que.put((-tmp, tmp))

cnt = 0
for i in range(T):
    height = que.get()[1]

    if height < H:
        break
    elif height == 1:
        # que.put((-height, height))
        break
    elif height > 1:
        bbong = height // 2
        que.put((-bbong, bbong))
        cnt += 1

max_height = 1 if que.empty() else que.get()[1]

if cnt <= T and max_height < H:
    print(f'YES\n{cnt}')
else:
    print(f'NO\n{max_height}')