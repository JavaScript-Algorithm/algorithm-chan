function solution(priorities, location) {
    const orders = [...new Array(priorities.length)].map((e, i) => i);
    const result = [];
    
    while (priorities.length !== 0) {
        const front_p = priorities.shift();
        const front_o = orders.shift();
        if (priorities.find(e => e > front_p)) {
            // 우선순위 높은게 있는 경우 뒤로 push
            priorities.push(front_p);
            orders.push(front_o);
        } else {
            // 우선순위 제일 높으면 result에 push
            result.push(front_o);
        }
    }
    
    // result에서 location의 index 탐색
    return result.indexOf(location) + 1
}