function combination(items, idx, k, list, result) {
    if(items.length === k) {
      result.push(items);
      return;
    }
    for (let i = idx; i < list.length; i ++) {
      combination([...items, list[i]], i + 1, k, list, result);
    }
  }
  
  function solution(orders, course) {
      // 1. 조합으로 선택, 정렬 후 객체에 대입
      // order: count
      
      const ans = {} // order: count
      const answer = [];
      
      orders.forEach(order => {
          const orderAry = order.split('');
          
          // 코스 선택
          course.forEach(k => {
              let results = [];
              if (k <= orderAry.length) {
                  combination([], 0, k, orderAry, results);    
              }
              
              // 정렬 후 객체에 대입
              results.forEach(result => {
                  const menu = result.sort().join(''); 
                  if (!ans[menu]) ans[menu] = 1;
                  else ans[menu] += 1;
              })
          })
      })
      
      // 개수별로 count가 가장 많은 것만 뽑는다. 
      const ansAry = Object.entries(ans).filter(([key, value]) => value >= 2);
      course.forEach((len) => {
          // 코스 길이가 len인 것들만 필터링
          const candidate = ansAry.filter(([key, value]) => key.length === len);
          
          // 그 중 최대값 코스만 살아남음
          if (candidate.length > 0) {
              const counts = [];
              candidate.forEach(([key, count]) => counts.push(count))
              const max = Math.max(...counts)
  
              const ans_elem = candidate
                          .filter(([key, count]) => count === max)
                          .map(([key, count]) => key)
              answer.push(...ans_elem)
          }
      })
      answer.sort();
      return answer;
  }