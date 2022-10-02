function getPermutation(items, k, list, result) {
    if(items.length === k) {
      result.push(items);
      return;
    }
    for (let i = 0; i < list.length; i ++) {
      getPermutation([...items, list[i]], k, list.filter((v, j) => j !== i), result);
    }
  }
  
  function solution (n, weak, dist) {
    const len = weak.length;
    const linear_weak = new Array(len*2 - 1).fill(0);
  
    for(let i = 0; i < len*2-1; i++)
      linear_weak[i] = i < len ? weak[i] : weak[i-len] + n;
    
    for (let i = 1; i <= dist.length; i++) {
        const dists = [];
        getPermutation([], i, dist, dists);
        
        for(const dist of dists) {
            for(let j = 0; j < len; j++) {
              let line = linear_weak.slice(j, len+j);
              for(const friend_dist of dist) {
                const coverage = line[0] + friend_dist;
                line = line.filter(e => e > coverage);
                if(!line.length) return dist.length;
              }
            }
        }
    }
    
    return -1;
  }