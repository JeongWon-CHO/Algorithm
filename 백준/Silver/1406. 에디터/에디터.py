import sys
input = sys.stdin.readline

leftText = list(input().rstrip())
rightText = []

N = int(input())

for i in range(N):
  order = input().split()

  if len(order) == 2:  # $라는 문자를 커서 왼쪽에 추가함
    leftText.append(order[1])

  elif order[0] == 'L':  # 커서를 왼쪽으로 한 칸 옮김
    if len(leftText) > 0:
      tmp = leftText.pop()
      rightText.append(tmp)

  elif order[0] == 'D':  # 커서를 오른쪽으로 한 칸 옮김
    if len(rightText) > 0:
      tmp = rightText.pop()
      leftText.append(tmp)

  elif order[0] == 'B':  # 커서 왼쪽에 있는 문자를 삭제함 (커서가 문장의 맨 앞이면 무시됨)
    if len(leftText) > 0:
      leftText.pop()

result = leftText + rightText[::-1]
print(''.join(result))