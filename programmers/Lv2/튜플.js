function sortByLength(b, a) {
    if (a.length < b.length) return 1;
    else if (a.length > b.length) return -1;
    return 0;
}

function solution(s) {
    const flat = s
                 .slice(2, s.length - 2)
                 .split('},{')
                 .map(e => e.split(','))
                 .sort(sortByLength)
    
    const ans = [flat[0]];
    
    for (let i = 0; i < flat.length - 1; i++) {
        ans.push(flat[i + 1].filter(e => !flat[i].includes(e)))
    }
    
    return ans.flat().map(e => parseInt(e))
}