// 경로가 단 하나라도 겹치면 같은 경로
// 모든 경로는 하나라도 겹치지 않음
function solution(grid) {
    const result = [];
    
    // 각 좌표마다 크기가 4인 배열 삽입
    const cycle = grid
                   .map(row => row
                                .split('')
                                .map(_ => new Array(4).fill(false)));
    
    // up right down left
    const direct = [[-1,0], [0,1], [1,0], [0,-1]];
    
    // 3차원 배열의 각 원소는 [row][col]에서의 방향을 의미한다
    cycle.forEach((row, rdx) => {
        row.forEach((col, cdx) => {
            col.forEach((route, idx) => {
                if (!route) {
                    result.push(checkCycle(rdx, cdx, idx));
                }
            })
        })
    })
    
    function checkCycle(rdx, cdx, idx) {
        let result = 0;
        
        while(true) {
            if (cycle[rdx][cdx][idx]) break; // 방문했으면 순환이므로 멈춘다
            
            cycle[rdx][cdx][idx] = true; // 방문 처리
            result++;
            
            // 다음 좌표 구하기
            rdx += direct[idx][0];
            cdx += direct[idx][1];
            if (rdx < 0) rdx = cycle.length - 1;
            if (rdx >= cycle.length) rdx = 0;
            if (cdx < 0) cdx = cycle[0].length - 1;
            if (cdx >= cycle[0].length) cdx = 0;
            
            // 좌표값(방향) 구하기. 이는 다음 방향이 된다.
            // 방향 반전은 L, R 일때만 일어난다.
            if (grid[rdx][cdx] === 'L') idx = [3, 0, 1, 2][idx];
            if (grid[rdx][cdx] === 'R') idx = [1, 2, 3, 0][idx];
        }
        
        return result;
    }
    
    return result.sort((b, a) => b - a);
}