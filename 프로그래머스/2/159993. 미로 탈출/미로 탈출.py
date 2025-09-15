from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]

def OOB(y, x, n, m):
    return y<0 or x<0 or y>=n or x>=m

def BFS(stY, stX, board, target):
    N = len(board)
    M = len(board[0])
    
    q = deque()
    dist = [[-1] * M for _ in range(N)]
    
    q.append((stY, stX))
    dist[stY][stX] = 0
    
    flag = False  # 조건 만족 여부
    edY = stY
    edX = stX
    while q:
        curY, curX = q.popleft()
        
        for i in range(4):
            ny = dy[i] + curY
            nx = dx[i] + curX
            
            if OOB(ny, nx, N, M):
                continue
            elif dist[ny][nx] != -1:
                continue
            elif board[ny][nx] == 'X':
                continue
            elif board[ny][nx] == target:
                dist[ny][nx] = dist[curY][curX] + 1
                flag = True
                edY = ny
                edX = nx
                break
                     
            dist[ny][nx] = dist[curY][curX] + 1
            q.append((ny, nx))

        if flag:
            break

    return dist, edY, edX, flag


def solution(maps):
    startX = 0
    startY = 0
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                startX = j
                startY = i
                break

    leverDist, startY, startX, flagL  = BFS(startY, startX, maps, 'L')  # 시작점 ~ 레버 구하는 BFS
    
    if not flagL:  # 레버를 못 만났을 경우
        return -1
    
    tmp = leverDist[startY][startX]
    
    exitDist, endY, endX, flagE = BFS(startY, startX, maps, 'E')  # 레버 ~ 도착점 구하는 BFS
    
    if not flagE:  # 탈출구를 못 만났을 경우
        return -1
    
    result = exitDist[endY][endX] + tmp
    
    return result if result else -1