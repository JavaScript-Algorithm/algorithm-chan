function findZero(arr) {
    // arr에 0이 하나도 없으면 true, 아니면 false    
    for (let i = 0; i < arr.length; i++)
        for (let j = 0; j < arr[i].length; j++)
            if (!arr[i][j]) return [i, j];
    
    return [-1, -1]
}

function solution(n) {
    // cell의 개수는 n + (n-1) + (n-2) + ... + 1
    // 3단계로 이루어짐.
    // 왼쪽 테두리, 밑변, 오른쪽 테두리
    // 첫 시행은 직접 대입. 나머지부터는 규칙성 존재. 
    const cells = Array.from({length: n}, (_, i) => Array(i + 1).fill(0));
    
    // 첫 시작은 직접 대입
    let value = 1;
    
    for (let r = 0; r < n; r++) cells[r][0] = value++;
    for (let c = 1; c < n; c++) cells[n-1][c] = value++;
    for (let r = n-2; r > 0; r--) cells[r][cells[r].length - 1] = value++;
    
    // 모든 cell이 0이 아닐때까지 반복
    while (true) {
        // 3단계 수행
        let [zRow, zCol] = findZero(cells);
        if (zRow === -1) break;
        
        // zRow시작으로 0이 아닐때까지 반복
        while(!cells[zRow][zCol]) cells[zRow++][zCol] = value++;
        zCol++;
        zRow--;
        while(!cells[zRow][zCol]) cells[zRow][zCol++] = value++;
        zRow--;
        zCol -= 2;
        while(!cells[zRow][zCol]) cells[zRow--][zCol--] = value++;
    }
    
    return cells.flat();
}