function solution(n, left, right) {
    // 배열 크기는 right - left + 1
    
    const getCoordinate = (point) => {
        const row = Math.floor(point / n);
        const col = point % n;
        return [row, col];
    }
    
    const len = right - left + 1
    const arr = Array(len).fill(0);
    let idx = 0;
    
    for (let point = left; point <= right; point++) {
        const val = Math.max(...getCoordinate(point)) + 1;
        arr[idx] = val;
        idx++;
    }
    
    return arr;
}