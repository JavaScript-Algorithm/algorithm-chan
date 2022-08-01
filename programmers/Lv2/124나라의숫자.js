function solution(n) {
    // 3으로 나눈다
    // 나머지로 값 변환한다.
    // 나머지가 0이면 n = floor((n-1) / 3)
    // else n = n / 3
    let ans = '';
    
    const radix = ['4', '1', '2'];
    
    while (n > 0) {
        const remain = n % 3;
        ans = radix[remain] + ans;
        if (remain === 0) n = Math.floor((n - 1) / 3);
        else n = Math.floor(n / 3);
    }
    
    return ans;
}