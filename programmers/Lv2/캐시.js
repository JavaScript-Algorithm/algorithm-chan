function solution(cacheSize, cities) {
    if (cacheSize === 0) return 5 * cities.length
    
    // 1. lowercase 후 해시화
    const hash = {};
    cities = cities.map(e => e.toLowerCase());
    cities.forEach((e, i) => {
        if (!hash[e]) hash[e] = i;
    })
    
    let cache = [];
    let ans = 0;
    let cacheHit = true;
    cities.forEach(city => {
        const idx = cache.indexOf(city)
        if (idx !== -1) {
            // cache hit - 빼서 캐시 뒤로 push
            const tmp = cache[idx];
            cache.splice(idx, 1);
            cache.push(tmp);
            ans++;
        } else {
            // cache miss
            // 1) 공간 있으면 push
            // 2) 공간 없으면 shift, push
            if (cache.length === cacheSize) cache.shift();
            cache.push(city);
            ans += 5;
        }
    })
    
    return ans;
}