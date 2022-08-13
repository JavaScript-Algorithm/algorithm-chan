function solution(maps) {
    // bfs로 경로 탐색
    // 도착지에 도달하면 ans에 push
    // ans가 비었으면 -1, 아니면 최소값 반환
    const [row, col] = [maps.length, maps[0].length];
    
    const visited = maps.map(row => row.map(v => 0));
    visited[0][0] = 1;
    
    const queue = [[0, 0]];
    
    const dx = [0, 0, 1, -1];
    const dy = [1, -1, 0, 0];
    
    // bfs
    while(queue.length) {
        const [x, y] = queue.shift();
        
        for (let i = 0; i < 4; i++) {
            const xx = x + dx[i];
            const yy = y + dy[i];
            
            if (xx >= 0 && xx < maps.length && yy >= 0 && yy < maps[0].length) {
                if (!visited[xx][yy] && maps[xx][yy]) {
                    visited[xx][yy] = visited[x][y] + 1;
                    queue.push([xx, yy]);
                }
            }
        }
    }
    
    return visited[row-1][col-1] ? visited[row-1][col-1] : -1;
}