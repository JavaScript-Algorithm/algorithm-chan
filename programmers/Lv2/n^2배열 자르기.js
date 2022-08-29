function solution(n, left, right) {
    const arr = []
    
    for (let point = left; point <= right; point++) 
        arr.push(Math.max(Math.floor(point / n), point % n) + 1);
    
    return arr;
}