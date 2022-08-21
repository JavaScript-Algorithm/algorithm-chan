function solution(n, times) {
    let left = 0; 
    let right = times[times.length - 1] * n;
    let mid;
    times.sort();
    
    while(left <= right) {
        mid = Math.floor((left + right) / 2);
        
        const people = times
                      .map(t => Math.floor(mid / t))
                      .reduce((acc, cur) => acc + cur, 0);
        console.log(left, mid, right)
        if (people < n) left = mid + 1;
        else right = mid - 1;
    }
    return left;
}