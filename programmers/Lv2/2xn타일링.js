function solution(n) {
    const dp = [...new Array(n + 1)].fill(0);
    const DIVIDER = 1000000007;
    dp[0] = 1;
    dp[1] = 1;
    
    if (n === 1) return dp[1];
    else {
        for (let i = 2; i <= n; i++) {
            dp[i] = (dp[i - 1] + dp[i - 2]) % DIVIDER;
        }
    }
    
    return dp[n];
}