function isRightBracket(brackets) {
    const stack = [];
    
    for (let i = 0; i < brackets.length; i++) {
        if (brackets[i] === '(') {
            stack.push(brackets[i]);
            continue;
        } 
        
        const top = stack.length - 1;
        
        if (stack[top] === '(') stack.pop();
        else return false
    }
    
    return stack.length === 0;
}

// 두 균형 잡힌 괄호 문자열로 쪼개는 함수
function splitBrackets(brackets) {
    let check = 0;
    
    for (let i = 0; i < brackets.length; i++) {
        if (brackets[i] === '(') check++;
        else check--;
        
        if (check === 0) {
            return [brackets.slice(0, i + 1), brackets.slice(i + 1)] 
        }
    }
}
    
function solution(brackets) {
    if (brackets.length === 0) return brackets; // case 1
    
    let [u, v] = splitBrackets(brackets); // case2
    
    if (isRightBracket(u)) {
        return u + solution(v); // case3
    }
    
    else {
        const slicedReverse = u
            .slice(1, u.length - 1)
            .split('')
            .map(bracket => bracket === '(' ? ')' : '(')
            .join('')
        
        return '(' + solution(v) + ')' + slicedReverse;
    }
}