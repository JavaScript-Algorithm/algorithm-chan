const dijks = (start, dist, adj) => {
    const queue = [];
    
    queue.push({ to: start, cost: 0 });
    dist[start] = 0; // 출발 노드

    while (queue.length !== 0) {
        const { to, cost } = queue.shift();
        
        if (dist[to] < cost) continue;
        
        adj[to].forEach((next) => {
            if (dist[next.to] > dist[to] + next.cost) {
                dist[next.to] = dist[to] + next.cost;
                queue.push(next);
            }
        });
    }
}

function solution(n, s, a, b, fares) {   
    let dist = new Array(n).fill(Infinity);
    const adj = Array.from({length: n}, () => []);
    
    fares.forEach(([a, b, cost]) => {
        adj[a-1].push({ to: b-1, cost });
        adj[b-1].push({ to: a-1, cost });
    })
    
    // 1. s에서 다익스트라 구함. 각 지점의 값 저장
    dijks(s-1, dist, adj);
    console.log(dist);
    
    // 2. 각 지점에서 다익스트라 구함. 여기서 A + B
    const second_dist = [...dist].map((distance, i) => {
        // i를 다시 출발점으로 놓고 다익스트라
        dist = dist.map(e => Infinity);
        dijks(i, dist, adj);
        return distance + dist[a-1] + dist[b-1];
    })
    
    return Math.min(...second_dist)
}