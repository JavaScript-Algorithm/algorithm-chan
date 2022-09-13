def solution():
    n = int(input())
    schedule = [0] + [list(map(int, input().split())) for i in range(n)]
    dp = [0] * (n+2)
    
    for i in range(1, n+1):
        day, benefit = schedule[i]
        dp[i] = max(dp[i], dp[i-1])
        if i + day <= n+1:
            dp[i + day] = max(dp[i] + benefit, dp[i + day])
    
    print(max(dp))
    
solution()