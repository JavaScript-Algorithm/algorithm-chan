function solution(clothes) {
    const hash = {};
    
    // 1. [name, type] 들을 {type: [name]} 으로 정함
    clothes.forEach(([name, type]) => {
        if (!hash[type]) hash[type] = [name];
        else hash[type].push(name);
    })
    
    for (let key in hash) hash[key] = hash[key].length + 1;
    
    const list = Object.values(hash);
    
    // 2. lists의 숫자들을 곱하고 1 뺀게 정답
    return list.reduce((acc, cur) => acc * cur, 1) - 1;
}