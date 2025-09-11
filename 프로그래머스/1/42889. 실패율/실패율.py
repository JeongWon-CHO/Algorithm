def solution(N, stages):
    tmp = [-1] + [0] * (N + 1)
    
    for i in stages: tmp[i] += 1
    
    stage = [(i, tmp[i] / sum(tmp[i::])) if sum(tmp[i::]) != 0 else (i, 0) for i in range(1, N+1)]
    
    stage = sorted(stage, key = lambda x: (-x[1], x[0]))
    
    answer = [x[0] for x in stage]
    
    return answer