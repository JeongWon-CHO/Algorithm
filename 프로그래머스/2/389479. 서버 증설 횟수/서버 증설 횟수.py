def solution(players, m, k):
    answer = 0
    server = [0] * len(players)
    
    for i in range(len(players)):
        if players[i] // m <= server[i]:
            continue
        
        tmp = players[i] // m - server[i]
        answer += tmp
        for j in range(i, i+k):
            if j < len(players):
                server[j] += tmp
    print(server)
    return answer