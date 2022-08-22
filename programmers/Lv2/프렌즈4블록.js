function solution(m, n, board) {
    board = board.map(e => e.split(''));
    
    const checkSquare = (positions) => {
        for (let i = 0; i < m - 1; i++) {
            for (let j = 0; j < n - 1; j++) {
                const ch = board[i][j];
                if (ch !== '') {
                    if (board[i + 1][j] === ch && 
                        board[i][j + 1] === ch && 
                        board[i + 1][j + 1] === ch) 
                    {
                        positions.push([i, j]);
                        positions.push([i + 1, j]);
                        positions.push([i, j + 1]);
                        positions.push([i + 1, j + 1]);
                    }
                }
            }
        }
        
        if (positions.length > 0) return true;
        return false;
    }
    
    while (true) {
        const positions = [];
        
        // 삭제 가능한지 검사
        if (!checkSquare(positions)) break;
        
        // position에 있는거 다 삭제
        positions.forEach(([row, col]) => board[row][col] = '')
        
        // board 이동 - 가장 아래부터 시작해서 ''이면 열 탐색
        for (let i = m - 1; i >= 0; i--) {
            for (let j = n - 1; j >= 0; j--) {
                if (board[i][j] === '') {
                    let change_row = i;
                    while (change_row >= 0 && board[change_row][j] === '') change_row--;
                    if (change_row >= 0) {
                        board[i][j] = board[change_row][j];
                        board[change_row][j] = '';
                    }
                }
            }
        }
    }
    
    // 빈칸 세기
    return board.reduce((acc, cur) => {
        return acc + cur.filter(e => e === '').length;
    }, 0)
}