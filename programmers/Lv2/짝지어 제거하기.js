function solution(s) {
    // 비어있거나 top과 다르면 push
    // top과 같으면 pop
    
    const stack = [];
    
    Array.from(s).forEach(e => {
        if (stack.length === 0 || e !== stack[stack.length - 1]) stack.push(e);
        else stack.pop();
    })
    
    if (stack.length === 0) return 1;
    
    return 0;
}