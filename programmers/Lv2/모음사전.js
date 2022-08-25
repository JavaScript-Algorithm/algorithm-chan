function solution(word) {
    const dict = ["A", "E", "I", "O", "U"];
    let flag = true;
    ans = 0;
    
    function dfs (w) {
        if (flag) {
            ans++;
            if (w === word) {
                flag = false;
                return;
            } 
            
            if (w.length < 5) {
                for (let ch of dict) {
                    dfs(w + ch)
                }      
            }
        }
    }
    dfs("");
    return ans - 1;
}