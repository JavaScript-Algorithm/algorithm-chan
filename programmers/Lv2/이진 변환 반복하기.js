function solution(s) {
    s = s.split('')
    let [trans_count, zero_count] = [0, 0];
    
    while (s.length !== 1) {
        // 1. 0 제거
        s = s.filter(e => {
            if (e === '1') return true;
            zero_count++;
            return false;
        })    
        
        // 2. 이진수 변환
        trans_count++;
        s = s.join('').length.toString(2).split('')
    }    
    
    return [trans_count, zero_count]
}