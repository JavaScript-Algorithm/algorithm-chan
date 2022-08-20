function solution(k, dungeons) {
    let ans = 0;
    const visit = dungeons.map(e => 0);
    
    const dfs = (k, cnt) => {
        ans = Math.max(ans, cnt);
        
        for(let i = 0; i < dungeons.length; i++) {
            if (k >= dungeons[i][0] && !visit[i]) {
                visit[i] = 1;
                dfs(k - dungeons[i][1], cnt + 1);
                visit[i] = 0;
            }
        }
    }
    
    dfs(k, 0);
    return ans;
}