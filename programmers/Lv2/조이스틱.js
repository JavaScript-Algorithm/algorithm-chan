// 개별 문자 조이스틱 최소 움직임 횟수
function joyStick(char) {
    const [A, Z, c] = ['A', 'Z', char].map(e => e.charCodeAt());
    return Math.min(Math.abs(c - A), Math.abs(Z - c + 1));
}

// 모든 A의 시작 인덱스와 끝 인덱스 찾아서 반환
function get_Aindexes(name) {
    let idx = 0; // 탐색 시작점
    const Aindexes = [];
    while(name.includes('A', idx)) {
        const start_idx = name.indexOf('A', idx); // 'A' 시작 인덱스
        let end_idx = start_idx; // 'A' 끝 인덱스
        while(name[end_idx + 1] === 'A') end_idx++;
        
        Aindexes.push([start_idx, end_idx]);
        
        idx = end_idx + 1; // 다음 A 탐색의 시작점
    }
    
    return Aindexes;
}


function solution(name) {
    // 모든 문자가 A인 경우
    if (name.split('').every(c => c === 'A')) return 0;
    
    // 각 문자별 조이스틱 움직인 횟수 합
    const unitMove_sum = name
                        .split('')
                        .map(joyStick)
                        .reduce((acc, cur) => acc + cur, 0);
    
    // 문자간 이동합
    const move_sum = Math.min(
        name.length - 1, // A가 없는 경우
        ...get_Aindexes(name)
            .map(([start, end]) => {
            const left = start - 1 >= 0 ? start - 1 : 0; // A chunk 왼쪽 이동 횟수
            const right = Math.abs(name.length - 1 - end); // A chunk 오른쪽 이동 횟수
            return left + right + Math.min(left, right);
        }))
    
    return unitMove_sum + move_sum;
}