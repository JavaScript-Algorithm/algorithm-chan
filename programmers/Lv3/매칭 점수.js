function solution(word, pages) {
    // 나의 링크를 key로 쓴다
    // vlaue = 인덱스, 페이지별 기본 점수, 외부 링크 배열
    
    // meta 태그가 아니면서 링크를 가질 수 있음. 
    // 따라서 meta~content 까지를 반드시 포함해야함
    const keyReg = /<meta property="og:url" content="\b[^>]*"/gi;
    const linksReg = /a href="\b[^>]*"/gi;
    
    word = word.toLowerCase();
    
    const hash = {};
    pages.forEach((page, index) => {
        page = page.toLowerCase();
        let key = page.match(keyReg)[0]
                      .split('"')[3]
        
        let links = page.match(linksReg);
        links !== null ?
        links = links.map(e => e.split('"')[1]) :
        links = [];     
        
        const baseScore = page.replace(/(<([^>]+)>)/ig,"")
                              .split(/[^a-z]/gi)
                              .filter(e => e === word)
                              .length;
        
        hash[key] = { index, links, baseScore};
    })
  
    const score = pages.map(e => 0);
    
    for (let key in hash) {
        // pages[index] = totalScore
        // index: hash[key][index]
        const { index, links, baseScore } = hash[key];
        score[index] += baseScore;
        
        const outerLinkScore = baseScore / links.length;
              
        for (let link of links) {
            if (hash[link]) {
                score[hash[link].index] += outerLinkScore
            }
        }
    }
    
    let max_idx = 0;
    score.forEach((s, i) => {
        if (score[max_idx] < s) {
            max_idx = i;
        }
    })
    
    return max_idx
}
