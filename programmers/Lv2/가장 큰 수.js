function solution(numbers) {
    if (numbers.every(e => e === 0)) return '0';
    
    return numbers
        .map(e => e.toString())
        .sort((b, a) => {
            if (a + b > b + a) return 1;
            else if (a + b < b + a) return -1;
            return 0;
        })
        .join('')
}