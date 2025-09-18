from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]

def OOB(y, x, n, m):
    return y<0 or x<0 or y>=n or x>=m

def BFS(stY, stX, board, refactorBoard, days):
    n = len(board)
    m = len(board[0])
    
    dist = [[-1] * m for _ in range(n)]
    q = deque()
    
    dist[stY][stX] = days
    q.append((stY, stX))
    
    tmpDays = days
    while q:
        curY, curX = q.popleft()
        
        for i in range(4):
            ny = curY + dy[i]
            nx = curX + dx[i]
            
            if OOB(ny, nx, n, m):
                continue
            if dist[ny][nx] != -1:
                continue
            if board[ny][nx] == 'X':
                continue
                
            dist[ny][nx] = dist[curY][curX] + 1
            q.append((ny, nx))
            
            tmpDays += int(board[ny][nx])
            refactorBoard[ny][nx] = False
    
    return tmpDays

def solution(maps):
    refactorMaps = [[True] * len(maps[0]) for _ in range(len(maps))]
    
    answer = []
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != 'X' and refactorMaps[i][j]:
                answer.append(BFS(i, j, maps, refactorMaps, int(maps[i][j])))
    
    if len(answer) > 0:
        answer.sort()
    else:
        answer.append(-1)
        
    return answer