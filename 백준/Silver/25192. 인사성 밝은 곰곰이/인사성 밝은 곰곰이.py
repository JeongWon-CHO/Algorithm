N = int(input())
person = [input() for _ in range(N)]

record = set()
cnt = 0
for i in person:
    if i == 'ENTER':
        cnt += len(record)
        record = set()
    else:
        record.add(i)

cnt += len(record)
print(cnt)