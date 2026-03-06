def solution(triangle):
    answer = 0
    N = len(triangle)
    
    dp = [[0 for _ in range(i)] for i in range(1, N+1) ]
    
    dp[0][0] = triangle[0][0]
    
    dp[1][0] = triangle[0][0] + triangle[1][0]
    dp[1][1] = triangle[0][0] + triangle[1][1]
    
    for i in range(2, N):
        for j in range(i+1):
            if j == 0:
                dp[i][j] = dp[i-1][0] + triangle[i][j]
            elif j == i:
                dp[i][j] = dp[i-1][-1] + triangle[i][j]
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
            
    answer = (max(dp[-1]))
            
    
    return answer