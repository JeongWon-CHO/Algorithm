def check_top(i, j, place):
    if 0 <= i-1:
        if place[i-1][j] == 'X':
            return 1
        elif place[i-1][j] == 'P':
            return 0
        else:
            if 0 <= i-2:
                if place[i-2][j] == 'P':
                    return 0
                else:
                    return 1
            else:
                return 1
    else:
        return 1
    
def check_bottom(i, j, place):
    if i+1< 5:
        if place[i+1][j] == 'X':
            return 1
        elif place[i+1][j] == 'P':
            return 0
        else:
            if i+2< 5:
                if place[i+2][j] == 'P':
                    return 0
                else:
                    return 1
            else:
                return 1
    else:
        return 1
    
def check_left(i, j, place):
    if 0 <= j-1:
        if place[i][j-1] == 'X':
            return 1
        elif place[i][j-1] == 'P':
            return 0
        else:
            if 0 <= j-2:
                if place[i][j-2] == 'P':
                    return 0
                else:
                    return 1
            else:
                return 1
    else:
        return 1
    
def check_right(i, j, place):
    if j+1 < 5:
        if place[i][j+1] == 'X':
            return 1
        elif place[i][j+1] == 'P':
            return 0
        else:
            if j+2 < 5:
                if place[i][j+2] == 'P':
                    return 0
                else:
                    return 1
            else:
                return 1
    else:
        return 1
            

def solution(places):
    answer = []
    
    for place in places:
        
        totalP = 0
        cnt = 0
        isBreak = False
        for i in range(5):
            if isBreak:
                break
                
            for j in range(5):
                if totalP != cnt:
                    isBreak = True
                    break
                    
                if place[i][j] == 'P':
                    # print(f'P = P[{i}][{j}]')
                    totalP += 1
                    
                    if not check_top(i, j, place):
                        # print(f'  place[{i}][{j}]: 위에서 문제 발생')
                        continue
                        
                    if not check_bottom(i, j, place):
                        # print(f'  place[{i}][{j}]: 아래에서 문제 발생')
                        continue
                        
                    if not check_left(i, j, place):
                        # print(f'  place[{i}][{j}]: 왼쪽에서 문제 발생')
                        continue
                    
                    if not check_right(i, j, place):
                        # print(f'  place[{i}][{j}]: 오른쪽에서 문제 발생')
                        continue
                        
                    # print(f'  place[{i}][{j}]: 우선 상하좌우 문제 없음!')
                    
                    # 대각선 확인
                    if 0 <= i-1 and j+1 < 5:
                        if place[i-1][j+1] == 'P':
                            if not (place[i-1][j] == 'X' and place[i][j+1] == 'X'):
                                continue
                    # print(f'                   -> 우측 상단 대각선 통과!')
                    
                    if i+1 < 5 and j+1 < 5:
                        if place[i+1][j+1] == 'P':
                            if not (place[i][j+1] == 'X' and place[i+1][j] == 'X'):
                                continue
                    # print(f'                   -> 우측 하단 대각선 통과!')
                                
                    if i+1 < 5 and 0 <= j-1:
                        if place[i+1][j-1] == 'P':
                            if not (place[i+1][j] == 'X' and place[i][j-1] == 'X'):
                                continue
                    # print(f'                   -> 좌측 하단 대각선 통과!')
                                
                    if 0 <= i-1 and 0 <= j-1:
                        if place[i-1][j-1] == 'P':
                            if not (place[i-1][j] == 'X' and place[i][j-1] == 'X'):
                                continue
                    # print(f'                   -> 좌측 상단 대각선 통과!')
                                
                    cnt += 1
        
        
        if totalP == cnt:
            answer.append(1)
        else:
            answer.append(0)
        
        print()
        print()
        print()
        
                    
    return answer