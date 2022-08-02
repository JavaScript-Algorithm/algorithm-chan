function solution(numbers, target) {
    let len = numbers.length;
    let ans = 0;
    
    function search(idx, val) {
        if (idx < len) {
            search(idx + 1, val + numbers[idx]);
            search(idx + 1, val - numbers[idx]);
        } else {
            if (val === target) {
                ans++;
            }
        }
    }
    
    search(0, 0);
    
    return ans;
}

