function solution(arr) {
    let [zero, one] = [0, 0];
    
    const quadTree = (point, len) => {
        const [x, y] = point;
        
        if (len === 1) {
            arr[x][y] === 0 ? zero++ : one++;
            return;
        }
        
        const halfLen = len / 2;
        const [xMid, yMid] = [x + halfLen, y + halfLen];
        
        const pivot = arr[x][y];
        let flag = false;
        for (let r = x; r < x + len; r++) {
            for (let c = y; c < y + len; c++) {
                if (arr[r][c] !== pivot) {
                    flag = true;
                    break;
                }
            }
            if (flag) break;
        }
        
        if (!flag) {
            pivot === 0 ? zero++ : one++;
            return;
        }
        
        quadTree([x, y], halfLen);
        quadTree([xMid, y], halfLen);
        quadTree([x, yMid], halfLen);
        quadTree([xMid, yMid], halfLen);
    }
    
    quadTree([0, 0], arr.length);
    
    return [zero, one]
}