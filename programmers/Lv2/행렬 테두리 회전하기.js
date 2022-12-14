function rotate(map, query) {
    // 순회 및 큐에 대입
    // 1. y1 ~ y2 (x1 고정)
    // 2. x1 ~ x2 (y2 고정)
    // 3. y2 ~ y1 (x2 고정)
    // 4. x2 ~ x1 (y1 고정)
    const queue = [];
    const [x1, y1, x2, y2] = query.map(e => e - 1);
    
    for (let c = y1; c <= y2; c++) queue.push(map[x1][c])
    for (let r = x1 + 1; r <= x2; r++) queue.push(map[r][y2]);
    for (let c = y2 - 1; c >= y1; c--) queue.push(map[x2][c]);
    for (let r = x2 - 1; r >= x1 + 1; r--) queue.push(map[r][y1]);
    
    const min_val = Math.min(...queue);
    queue.unshift(queue.pop());
    
    // 회전 
    for (let c = y1; c <= y2; c++) map[x1][c] = queue.shift();
    for (let r = x1 + 1; r <= x2; r++) map[r][y2] = queue.shift();
    for (let c = y2 - 1; c >= y1; c--) map[x2][c] = queue.shift();
    for (let r = x2 - 1; r >= x1 + 1; r--) map[r][y1] = queue.shift();
    
    return min_val;
}

function solution(rows, columns, queries) {
    // 배열 생성
    const map = [...Array(rows)]
                    .map((_, r) => [...Array(columns)]
                    .map((_, c) => r * columns + c + 1));
    
    const ans = [];
    queries.forEach(query => {
        ans.push(rotate(map, query));
    })
                    
    return ans;
}