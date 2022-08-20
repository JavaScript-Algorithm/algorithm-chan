function solution(number, k) {
    number = number.split('');
    const stack = [];
    
    // number에서 stack에 숫자 넣다가 새로운 숫자가 stack의 top보다 크면 pop한다.
    number.forEach((num) => {
        while (stack.length > 0 && stack[stack.length - 1] < num && k > 0) {
            k--;
            stack.pop();
        }
        stack.push(num);
    })
    
    // k가 남았으면 뒤에서 k만큼 뺀다
    if (k > 0) return stack.slice(0, stack.length - k).join('')    
    
    return stack.join('')
}