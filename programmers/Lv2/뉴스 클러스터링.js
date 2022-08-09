function get_chunk(str) {
    // 1. toLowerCase
    // 2. 두 글자씩 끊는다.
    // 3. 영문인 것들만 필터링
    str = str.toLowerCase();
    const chunks = [];
    const regex = /[a-z]{2}/ 
    for (let i = 0; i < str.length - 1; i++) {
        const chunk = str.slice(i, i + 2);
        if (regex.test(chunk)) chunks.push(chunk)
    }
    return chunks;
}

function solution(str1, str2) {
    const MULT = 65536;
    str1 = get_chunk(str1)
    str2 = get_chunk(str2)
    
    // 1. 교집합 판별 
    str1_set = [...new Set(str1)]
    let intersect = 0;
    str1_set.forEach(e => {
        filt1 = str1.filter(v => v === e).length;
        filt2 = str2.filter(v => v === e).length;
        intersect += Math.min(filt1, filt2);
    })
    
    // 2. 합집합 판별
    all_set = [...new Set([...str1, ...str2])];
    let union = 0;
    all_set.forEach(e => {
        filt1 = str1.filter(v => v === e);
        filt2 = str2.filter(v => v === e);
        union += Math.max(filt1.length, filt2.length);
    })
    
    if (union === 0) return MULT;
    
    return parseInt(MULT * (intersect / union));
}