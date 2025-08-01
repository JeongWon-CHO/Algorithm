text = input().split(':')
changes = []

zeroCount = text.count('')
# print(zeroCount)
# 전체 text 길이에서 zero를 빼면 일반 숫자의 갯수가 나옴
# 을 8에서 빼면 채워야되는 zero
totalZero = 8 - (len(text) - zeroCount)

flag = 1
for i in text:
    textLength = len(i)
    if textLength == 0 and flag:
        for j in range(totalZero):
            changes.append('0000')
        flag = 0
    elif 0 < textLength < 4:
        tmp = i.zfill(4)
        changes.append(tmp)
    else:
        changes.append(i)

for i in changes:
    if i == '':
        changes.remove(i)

result = ":".join(changes)
print(result)
