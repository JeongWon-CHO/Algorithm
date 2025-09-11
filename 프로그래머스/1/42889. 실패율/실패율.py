def solution(N, stages):
    result = {}
    total = len(stages)
    
    for stage in range(1, N+1):
        if total != 0:
            cnt = stages.count(stage)
            result[stage] = cnt / total
            total -= cnt
        else:
            result[stage] = 0
    
    return sorted(result, key=lambda x: (-result[x], x))