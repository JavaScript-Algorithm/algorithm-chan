function solution(expression) {
    const ans = [];
    
    // 1. 우선순위 *+- *-+ -+* -*+ +-* +*-
    const prior = ['*+-', '*-+', '-+*', '-*+', '+-*', '+*-'];

    // 2. expression을 연산자 기준 split
    const exp_ary = expression.split(/(\D)/);
    
    // 3. 우선순위별로 연산하고 결과값의 절대값의 최대값을 반환
    prior.forEach(operators => {
        const tmp = [...exp_ary];
        operators.split('').forEach(operator => {
            // tmp 내부의 연산자를 연산
            while(tmp.includes(operator)) {
                // index ~ index + 2 를 결과값으로 대체
                const idx = tmp.indexOf(operator);
                const calc = eval(tmp.slice(idx - 1, idx + 2).join(''));
                tmp.splice(idx - 1, 3, calc);
            }
        })
        ans.push(Math.abs(tmp[0]))
    })
    
    return Math.max(...ans);
}