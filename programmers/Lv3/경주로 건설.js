// 실패
function solution(board) {
    const len = board.length;
    const queue = [];
    const dx = [-1, 0, 1, 0];
    const dy = [0, -1, 0, 1];
    
    // 3차원 배열 생성 (방향 고려)
    const arr = board.map(r => r.map(c => Array(4).fill(Infinity)))
    
    for(let i = 0 ; i < 4 ; i++) {
        arr[0][0][i] = 0;    
        queue.push([0,0,i,0]);
    } 

    while(queue.length){
        const [x, y, dir, cost] = queue.shift(); 

        for(let i = 0; i < 4; i++){
            const nx = x+dx[i];
            const ny = y+dy[i];
            
            if(Math.abs(dir-i) === 2) continue; // 반대방향 금지
            if(nx < 0 || ny < 0 || nx >= len || ny >= len || board[nx][ny] === 1) continue;
            
            let next_cost = dir === i ? 100 : 600;
            let cost_sum = cost + next_cost;
            
            // 이동하는게 이득이면 비용 갱신 후 push
            if (arr[nx][ny][i] > cost_sum){
                arr[nx][ny][i] = cost_sum;
                queue.push([nx,ny,i,arr[nx][ny][i]]);
            }
        }
    }
    
    return Math.min(...arr[len-1][len-1]);
}