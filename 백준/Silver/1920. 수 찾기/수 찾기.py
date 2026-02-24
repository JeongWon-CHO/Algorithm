N = int(input())
ns = list(map(int, input().split()))

A = dict()
for i in ns:
    A[i] = 1

M = int(input())
ms = list(map(int, input().split()))

for i in ms:
    if i in A:
        print(1)
    else:
        print(0)