function rotate_key(key, dir) {
    const col_len = key[0].length;
    const row_len = key.length;
    const new_key = Array.from({ length: col_len }, () => Array(row_len).fill(0))
    for (let col = 0; col < col_len; col++) 
        for (let row = 0; row < row_len; row++) 
            new_key[col][row_len - 1 - row] = key[row][col];

    return new_key;
}

const isAnswer = (newLock, len) => {
  for (let i = len; i < len * 2; i++) {
    for (let j = len; j < len * 2; j++) {
      if (newLock[i][j] !== 1) {
        return false;
      }
    }
  }
  return true;
};

function solution(key, lock) {
    // lock * 3 짜리 배열 생성
    const len = lock.length;
    const spanLock = Array.from({length: len * 3}, () => Array(len * 3).fill(0));
    for (let i = 0; i < len; i++) 
        for (let j = 0; j < len; j++) 
            spanLock[i + len][j + len] = lock[i][j];    

    // key 네 번 회전
    // 회전할때마다 또 네 번 shift하고 검사
    const offset = spanLock.length - key.length + 1;
    for (let rotate = 0; rotate < 4; rotate++) {
        key = !rotate ? key : rotate_key(key, rotate); // 회전
        // spanLock의 (0,0)부터 차례대로 탐색
        for (let i = 0; i < offset; i++) {
            for (let j = 0; j < offset; j++) {
                // lock에서 key 면적만큼 비교
                const newLock = spanLock.map(arr => [...arr]);
                
                for (let r = 0; r < key.length; r++) {
                    for (let c = 0; c < key.length; c++) {
                        // key[r][c], lock[r+i][c+j]
                        newLock[i + r][j + c] += key[r][c];
                    }
                }
                if (isAnswer(newLock, len)) return true;
            }
        }
    }

    return false;
}