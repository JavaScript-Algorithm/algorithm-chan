function solution(N, road, K) {
    // dist 배열 생성
    const dist = Array(N).fill(Number.MAX_SAFE_INTEGER);
    const map = Array.from({length: N}, () => []);
    
    road.forEach(([a, b, time]) => {
        map[a - 1].push({to: b - 1, time});
        map[b - 1].push({to: a - 1, time});
    })
    
    const queue = [{to: 0, time: 0}];
    dist[0] = 0;
    
    while(queue.length) {
        const {to, time} = queue.pop();
        
        map[to].forEach((next) => {
            // 비용 검사
            if (dist[next.to] > dist[to] + next.time){
                dist[next.to] = dist[to] + next.time;
                queue.push(next);
            }
        })
    }
    
    return dist.filter(e => e <= K).length;
}