function isPrime(num) {
    if (num === 1 || num === 0) return false;
    if (num === 2 || num === 3) return true;
    
    for (let i = 2; i <= Math.sqrt(num); i++) {
        if (num % i === 0) return false;
    }
    return true;
}

function permutation(items, k, list, result) {
  if(items.length === k) {
    result.push(items);
    return;
  }
  for (let i = 0; i < list.length; i ++) {
    permutation([...items, list[i]], k, list.filter((v, j) => j !== i), result);
  }
}

function solution(numbers) {
    const list = numbers.split('').map(e => parseInt(e))
    const result = [];
    
    for (let i = 1; i <= list.length; i++) {
        permutation([], i, list, result);
    }
    
    return [...new Set(result.map(e => parseInt(e.join(''))))]
                .filter(e => isPrime(e))
                .length
}