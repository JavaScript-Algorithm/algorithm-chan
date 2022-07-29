function solution(str) {
    let answer = 1000;
    
    // 1이면 max_check 0이 되므로 ceil 처리
    const max_check = Math.ceil(str.length / 2);
    
    for (let i = 1; i <= max_check; i++) {
        const bundle = i;
        
        let compressed_word = '';
        let prev_cluster = str.slice(0, i);
        let cluster = '';
        let same_count = 0;
        
        for(let i = 0; i < str.length; i += bundle) {
            cluster = str.slice(i, i + bundle); 
            
            if (cluster === prev_cluster) {
                // 같으면 same_count++, prev_cluster 그대로
                same_count++;
            } else {
                // 다르면 저장 후 same_count = 0, prev_cluster 갱신
                same_count === 1 ? 
                compressed_word += prev_cluster :  
                compressed_word += `${same_count}${prev_cluster}`   
                
                same_count = 1; 
                prev_cluster = cluster;
            }
        }
        
        // 마지막에 검사하지 않은 cluster 검사 
        same_count === 1 ? 
        compressed_word += prev_cluster :  
        compressed_word += `${same_count}${prev_cluster}`   
        
        
        answer = Math.min(answer, compressed_word.length)
    }
    
    return answer;
}