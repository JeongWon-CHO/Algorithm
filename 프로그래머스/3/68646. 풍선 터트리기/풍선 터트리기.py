def solution(a):
    answer = 2
    
    if 0<= len(a) <= 2:
        return len(a)
    
    leftM = a[0]
    rightM = a[-1]
    
    for i in range(1, len(a)-1):
        if a[i] < leftM:
            answer += 1
            leftM = a[i]
        if a[-1-i] < rightM:
            answer += 1
            rightM = a[-1-i]
        
    return answer-1 if leftM == rightM else answer