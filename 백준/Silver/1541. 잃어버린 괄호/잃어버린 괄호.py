import sys
input = sys.stdin.readline

N = input().rstrip()

expr = N.split('-')

complete = []
for i in expr:
    if '+' in i:
        tmp_list = i.split('+')
        tmp = 0
        for j in tmp_list:
            tmp += int(j)
        complete.append(tmp)
    else:
        complete.append(int(i))

result = complete[0]
for i in range(1, len(complete)):
    result -= complete[i]

print(result)
