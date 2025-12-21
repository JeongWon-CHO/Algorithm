T = int(input())

for _ in range(T):

    N = int(input())
    stock = list(map(int, input().split()))  # [10, 7, 6]

    money = 0
    curMax = -1
    for i in range(len(stock)-1, -1, -1):
        if stock[i] > curMax:
            curMax = stock[i]
        else:
            money += curMax - stock[i]

    print(money)