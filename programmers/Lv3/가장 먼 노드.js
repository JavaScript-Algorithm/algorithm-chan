function solution(n, edge) {
    const visit = new Array(n + 1).fill(0);
    
    // nodes[i] = i번 노드와 인접한 노드 모음
    const nodes = [...visit].map(e => new Set());
    edge.forEach(([a, b]) => {
        nodes[a].add(b);
        nodes[b].add(a)
    })
    
    visit[1] = 1;
    const queue = [1];
    
    while(queue.length) {
        const front = queue.shift();
        
        for (let node of nodes[front]) {
            if (!visit[node]) {
                visit[node] = visit[front] + 1;
                queue.push(node);
            }
        }
    }
    
    const max = Math.max(...visit);
    return visit.filter(e => e === max).length;
}