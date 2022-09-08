function solution(stones, k) {
    // 이분탐색
    // 건널 수 있는 인원 1 ~ 2억
    let [left, right] = [1, 200000000];
    let mid;
    
    while(left <= right) {
        mid = Math.floor((left + right) / 2);
                
        // 연속된 0을 계속 찾는다.
        let count = 0;
        let flag = false;
        for (let stone of stones) {
            count = stone - mid <= 0 ? count + 1 : 0;
            
            if (count === k) {
                flag = true;
                break;
            }
        }
        
        // 연속된 0이 k이면 right 갱신해줘야 한다.
        // 연속된 0이 전부 k 이하면 left 갱신해준다.
        flag ? right = mid - 1 : left = mid + 1;
    }
    
    return left;
}