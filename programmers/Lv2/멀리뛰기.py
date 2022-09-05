def solution(n):
    # 1
    # 2
    # 3
    # 5
    # 8
    dp = [0 for i in range(n+2)]
    dp[0] = dp[1] = 1
    
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n] % 1234567