function solution(n) {
    const len = n.toString(2).replace(/0/g, '').length;
    
    while(++n) {
        const new_len = n.toString(2).replace(/0/g, '').length;
        if (new_len === len) break;
    }
    
    return n;
}