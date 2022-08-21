// 못풀어서 블로그 참고 - https://gurumee92.tistory.com/164
function solution(N, number) {
    const cache = [...new Array(9)].map(e => new Set());
    // cache[i] 는 i 개의 N으로 만들 수 있는 모든 숫자 집합
    
    for (let i = 1; i < 9; i++) {
        cache[i].add('1'.repeat(i) * N);
        for (let j = 1; j < i; j++) {
            for (let arg1 of cache[j]) {
                for (let arg2 of cache[i - j]) {
                    cache[i].add(arg1 + arg2);
                    cache[i].add(arg1 - arg2);
                    cache[i].add(arg1 * arg2);
                    if (arg2 !== 0) {
                        cache[i].add(arg1 / arg2)
                    }
                }
            }
        }
        if (cache[i].has(number)) return i;
    }
    
    return -1;
}