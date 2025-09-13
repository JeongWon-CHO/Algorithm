def solution(board, moves):
    answer = 0
    N = len(board)
    newBoard = []  # 스택
    result = []  # 뽑은 거 모아두는 스택
    
    for j in range(N):  # 행열 전환
        tmp = []
        for i in range(N-1, -1, -1):
            if board[i][j] != 0:
                tmp.append(board[i][j])
        newBoard.append(tmp)
    
    for pos in moves:
        if len(newBoard[pos-1]) <= 0:
            continue
        else:
            draw = newBoard[pos-1].pop()  # 인형을 뽑아!
            
            if len(result) == 0:  # 빈칸이면 무조건 넣어
                result.append(draw)
            elif draw == result[-1]:
                result.pop()
                answer += 2        
            else:
                result.append(draw)
        
    return answer