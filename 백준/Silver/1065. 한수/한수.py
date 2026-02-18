N = int(input())

cnt = 0
for i in range(1, N + 1):
    s = str(i)

    if len(s) <= 2:
        cnt += 1
        continue

    tmp = int(s[1]) - int(s[0])
    flag = True
    for j in range(2, len(s)):
        if int(s[j]) - int(s[j-1]) != tmp:
            flag = False
            break

    if flag:
        cnt += 1

print(cnt)