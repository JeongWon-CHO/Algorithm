import heapq

def solution(n, works):
    answer = 0
    
    result = []  # 최대 heap
    for i in works:
        heapq.heappush(result, -i)
    
    for i in range(n):
        tmp = heapq.heappop(result)
        if tmp != 0:
            heapq.heappush(result, -((-tmp)-1))
        else:
            heapq.heappush(result, 0)
        
    for i in result:
        answer += i**2
        
    return answer