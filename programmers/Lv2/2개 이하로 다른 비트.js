// 실패 - https://parkparkpark.tistory.com/m/103
function solution(numbers) {
    const getAns = (number) => {
        const number2 = ('0' + number.toString(2)).split('');
        if (number % 2 === 0) {
            number2.pop();
            number2.push('1');
        } else {
            const lastIndex = number2.lastIndexOf('0');
            number2[lastIndex] = 1;
            number2[lastIndex + 1] = 0;
        }
        return parseInt(number2.join(''), 2);
    }
    
    return numbers.map(getAns)
}