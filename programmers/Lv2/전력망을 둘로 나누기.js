function bfs(i, visit, adj) {
    const queue = [i];
    visit[i] = 1;
    let count = 1;
    
    while(queue.length) {
        const front = queue.shift();
        
        for (let node of adj[front]) {
            if (!visit[node]) {
                visit[node] = 1;
                queue.push(node);
                count++;
            }
        }
    }
    return count;
}

function solution(n, wires) {
    // 하나씩 제거하면서 비교
    let ans = 100;
        
    wires.forEach((_, i) => {
        const copy = wires.slice();
        copy.splice(i, 1);
        
        // 인접행렬 생성
        const adj = Array.from({length: n}, () => []);
        copy.forEach(([a, b]) => {
            adj[a-1].push(b-1);
            adj[b-1].push(a-1);
        })
        
        // bfs로 검사
        const visit = Array(n).fill(0);
        const dist = [];
        for (let i = 0; i < visit.length; i++) {
            if (!visit[i]) {
                dist.push(bfs(i, visit, adj))
            }
        }
        ans = Math.min(ans, Math.abs(dist[0] - dist[1]))
    })
    
    return ans;    
}