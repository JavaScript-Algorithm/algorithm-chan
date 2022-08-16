function solution(s) {
    const getBracket = {
        '[': ']',
        '{': '}',
        '(': ')'
    }
    let brackets = s.split('');
    let ans = 0;
    
    // 올바른 괄호인지 검사
    const isCorrectBrackets = (origin_brackets) => {
        const brackets = [...origin_brackets];
        const stack = [];
        
        for(let i = 0; i < brackets.length; i++) {
            const bracket = brackets[i];
            if (bracket === '(' || bracket === '{' || bracket === '[') {
                stack.push(bracket);
                continue;
            }
            
            // 비었으면 올바른 괄호 아님
            if (stack.length === 0) return false;
            else {
                const top = stack.pop();
                if (bracket !== getBracket[top]) return false;
            }
        }
        
        // 비었으면 올바른 괄호
        return stack.length === 0;
    }
    
    for (let i = 0; i < s.length; i++) {
        if (isCorrectBrackets(brackets)) ans++;
        brackets.push(brackets.shift())
    }
    
    return ans;
}