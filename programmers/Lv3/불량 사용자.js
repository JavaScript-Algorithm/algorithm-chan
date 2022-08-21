// 제제 id에 해당하는지 검사
function check(user, banned) {
    if (user.length !== banned.length) return false;
    for(let i = 0; i < user.length; i++) {
        if (banned[i] === '*') continue;
        if (banned[i] !== user[i]) return false;
    }
    return true;
}

function solution(user_id, banned_id) {
    // 1. banned_id를 가능한 아이디 수로 mapping
    // 2. 경우의 수가 1인거는 제외시킨다.
    // 3. 모든 숫자를 곱한다.
    banned_id = banned_id.map(banned => {
        const ary = [];
        user_id.forEach(user => {
            if (check(user, banned)) ary.push(user);
        })
        return ary;
    })
    
    const ans = new Set();
    
    const dfs = (row, list, items) => {
        if (items.length === list.length) {
            const items_set = [...new Set(items)];
            if (items_set.length === list.length) {
                ans.add([...items_set].sort().join(''))
            }
            return;
        }
        for (let i = 0; i < list[row].length; i++) {
            items.push(list[row][i]);
            dfs(row + 1, list, items);
            items.pop();
        }
    }
    
    dfs(0, banned_id, []);
    return ans.size;
}