N = int(input())

shortcut = []

for i in range(N):
    words = list(input().split())

    flag = True
    # 단어의 첫 글자가 이미 단축키로 지정되었는지 살펴본다
    answer = []
    for word in words:
        if flag and word[0].upper() not in shortcut:  # 단축키 가능
            shortcut.append(word[0].upper())
            answer.append('[' + word[0] + ']' + word[1:])
            flag = False
        else:
            answer.append(word)
    if not flag:
        print(' '.join(answer))

    # 왼쪽에서부터 차례대로 알파벳을 보면서 단축키로 지정
    if flag:
        answer2 = []
        flag2 = True
        check = True
        for word in words:
            tmp = ''

            if not flag2:
                answer2.append(word)
                continue

            for j in range(len(word)):
                if flag2 and word[j].upper() not in shortcut:  # 단축키 가능
                    answer2.append(tmp + '[' + word[j] + ']' + word[j+1:])
                    shortcut.append(word[j].upper())
                    flag2 = False
                    check = False
                    break
                else:
                    tmp += word[j]

                if j == len(word) - 1:
                    if len(answer2) == 0:
                        print(word)

        if not check:
            print(' '.join(answer2))