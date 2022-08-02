function solution(progresses, speeds) {
    const days = [];
    
    for(let i = 0; i < progresses.length; i++) {
        days.push(Math.ceil((100 - progresses[i]) / speeds[i]))
    }
    
    let today = days[0];
    let tomorrow = days[0];
    let count = 1;
    const ans = [];
    
    for(let i = 0; i < days.length - 1; i++) {
        tomorrow = days[i + 1];
        if (today >= tomorrow) {
            count++;
            continue;
        }
        
        ans.push(count);
        today = tomorrow;
        count = 1;
    }
    
    ans.push(count);
    
    return ans;
}